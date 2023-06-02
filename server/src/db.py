from langchain.embeddings import HuggingFaceEmbeddings 
from langchain.text_splitter import RecursiveCharacterTextSplitter
from langchain.vectorstores import Chroma
from server.src.server import TitleInfo

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

    def has(self, info: TitleInfo):
        print(self.vecstore.get())

    def add(self, text: str, info: TitleInfo):
        self.vecstore.add_texts(
            texts=self.splitter.split_text(text),
            metadata=info,
        )
        self.vecstore.persist()

    def search(self, query: str):
        docs = self.vecstore.similarity_search(query)

        if DEBUG:
            for chunk in docs: print(chunk, '\n')

        return list(set(map(lambda x: x.page_content, docs)))
