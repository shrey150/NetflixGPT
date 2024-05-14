
import pickle
from langchain.embeddings import HuggingFaceEmbeddings 
from langchain.text_splitter import RecursiveCharacterTextSplitter
from langchain.vectorstores import Chroma
from app.models import TitleInfo
from app.utils import hash_dict
from sqlmodel import Field, Session, SQLModel, create_engine, select

from dotenv import load_dotenv
from constants import *

import os

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

        # only needed for psycopg 3 - replace postgresql
        # with postgresql+psycopg in settings.DATABASE_URL

        self.connection_string = str(os.getenv("DB_CONNECTION_URI")).replace(
            "postgresql", "postgresql+psycopg"
        )

        # recycle connections after 5 minutes
        # to correspond with the compute scale down
        self.engine = create_engine(
            self.connection_string, connect_args={"sslmode": "require"}, pool_recycle=300
        )


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
        print("These are texts", texts)
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