from langchain.embeddings import HuggingFaceEmbeddings 
from langchain.text_splitter import RecursiveCharacterTextSplitter
from langchain.vectorstores import Chroma
from app.models import TitleInfo

from dotenv import load_dotenv
load_dotenv("../../.env")

PERSIST_DIR = 'db'
DEBUG = True

class Database():
    def __init__(self):
        self.embedding = HuggingFaceEmbeddings(model_name="all-MiniLM-L6-v2")
        self.splitter = RecursiveCharacterTextSplitter(chunk_size=1000, chunk_overlap=20)
        self.vecstore = Chroma(
            embedding_function=self.embedding,
            persist_directory=PERSIST_DIR
        )

    def get_all(self):
        data = self.vecstore.get()
        return list(zip(data['ids'], data['documents'], data['metadatas']))


    def add(self, text: str, info: dict):
        texts = self.splitter.split_text(str(text))
        self.vecstore.add_texts(
            texts=texts,
            metadatas=[info]*len(texts),
        )
        self.vecstore.persist()

    def search(self, query: str):
        docs = self.vecstore.similarity_search(query)
        return list(set(map(lambda x: x.page_content, docs)))
