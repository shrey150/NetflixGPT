
import pickle
from langchain.embeddings import HuggingFaceEmbeddings 
from app.models import TitleInfo
from app.utils import hash_dict
from sqlmodel import Field, Session, SQLModel, create_engine, select
from sqlalchemy.ext.asyncio import AsyncSession, create_async_engine
from sqlalchemy.orm import sessionmaker

from dotenv import load_dotenv
from constants import *

import os
from langchain_community.vectorstores import Chroma
from langchain_text_splitters import RecursiveCharacterTextSplitter

load_dotenv(DOTENV_PATH)
DEBUG = True

class Database():
    def __init__(self):
        self.embedding = HuggingFaceEmbeddings(model_name="all-MiniLM-L6-v2")
        self.splitter = RecursiveCharacterTextSplitter(chunk_size=1000, chunk_overlap=20)
        
        # TODO update this to Pinecone
        self.vecstore = Chroma(
            embedding_function=self.embedding,
            persist_directory=DB_PATH
        )

        # load cache from CACHE_PATH if file exists; else, initialize empty cache
        try:
            with open(CACHE_PATH, 'rb') as f:
                self.cache = pickle.load(f)
        except FileNotFoundError:
            self.cache = {}

        # update connection protocol for psycopg3
        self.connection_string = str(DB_CONNECTION_URI).replace(
            "postgresql", "postgresql+psycopg"
        )

        # recycle connections after 5 minutes
        # to correspond with the compute scale down
        self.engine = create_async_engine(
            self.connection_string,
            connect_args={"sslmode": "require"},
            pool_recycle=300
        )

        self.async_session = sessionmaker(
            self.engine,
            class_= AsyncSession,
            expire_on_commit=False,
        )

    async def create_db_and_tables(self):
        async with self.engine.begin() as conn:
            await conn.run_sync(SQLModel.metadata.create_all)

    async def async_get_db(self) -> AsyncSession:
        local_session = self.async_session

        async with local_session() as db:
            yield db
            await db.commit()

    def get_all(self):
        data = self.vecstore.get()
        return list(zip(data['ids'], data['documents'], data['metadatas']))

    def dict_get_all(self):
        data = self.get_all()
        d = {}
        d["data"] = data
        return d


    def has(self, info: dict):
        return hash_dict(info) in self.cache


    def add(self, text: str, info: dict):
        texts = self.splitter.split_text(str(text))
        self.vecstore.add_texts(
            texts=texts,
            metadatas=[info]*len(texts),
        )
        self.cache[hash_dict(info)] = True
        self._save_cache()
        self.vecstore.persist()


    def search(self, query: str, info: dict):
        docs = self.vecstore.similarity_search(query, filter={'title': info['title']})
        return list(set(map(lambda x: x.page_content, docs)))
    

    def _save_cache(self, path=CACHE_PATH):
        with open(path, 'wb') as f:
            pickle.dump(self.cache, f)


    def __del__(self):
        try:
            self._save_cache()
            self.vecstore.persist()
        except NameError as e:
            if e.name == 'open':
                pass
            else:
                print(f"Error: {e}")