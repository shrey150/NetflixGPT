import pickle
from langchain.embeddings import HuggingFaceEmbeddings 
from langchain.text_splitter import RecursiveCharacterTextSplitter
from langchain.vectorstores import Chroma
from app.models import TitleInfo
from app.utils import hash_dict

from dotenv import load_dotenv

load_dotenv("../../.env")

PERSIST_DIR = 'db'
CACHE_PATH = 'db_cache.pickle'
DEBUG = True

class Database():
    def __init__(self):
        self.embedding = HuggingFaceEmbeddings(model_name="all-MiniLM-L6-v2")
        self.splitter = RecursiveCharacterTextSplitter(chunk_size=1000, chunk_overlap=20)
        self.vecstore = Chroma(
            embedding_function=self.embedding,
            persist_directory=PERSIST_DIR
        )

        # load cache from CACHE_PATH if file exists; else, initialize empty cache
        try:
            with open(CACHE_PATH, 'rb') as f:
                self.cache = pickle.load(f)
        except FileNotFoundError:
            self.cache = {}


    def get_all(self):
        data = self.vecstore.get()
        return list(zip(data['ids'], data['documents'], data['metadatas']))


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
        self._save_cache()
        self.vecstore.persist()