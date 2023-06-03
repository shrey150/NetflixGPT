from chromaviz import visualize_collection
from langchain.vectorstores import Chroma
from app.db import Database

db = Database()
db.get_all()