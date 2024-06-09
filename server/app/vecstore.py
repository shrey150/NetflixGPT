
from langchain_text_splitters import RecursiveCharacterTextSplitter, SentenceTransformersTokenTextSplitter
from langchain_pinecone import PineconeVectorStore
from pinecone import Pinecone
from sentence_transformers import SentenceTransformer
from langchain_huggingface import HuggingFaceEmbeddings
from config import settings

embeddings = HuggingFaceEmbeddings(model_name="all-mpnet-base-v2")

text_splitter = RecursiveCharacterTextSplitter(
    separators=[
        "\n\n",
        "\n",
        " ",
        ".",
        ",",
        "\u200b",  # Zero-width space
        "\uff0c",  # Fullwidth comma
        "\u3001",  # Ideographic comma
        "\uff0e",  # Fullwidth full stop
        "\u3002",  # Ideographic full stop
        "",
    ],
    chunk_size=1024,
    chunk_overlap=0
)

vecstore = PineconeVectorStore(
    index_name="netflixgpt",
    embedding=embeddings,
    pinecone_api_key=settings.PINECONE_API_KEY
)

pinecone = Pinecone(api_key=settings.PINECONE_API_KEY)
index = pinecone.Index("netflixgpt")
