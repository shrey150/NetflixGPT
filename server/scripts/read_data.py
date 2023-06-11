import pickle
from pprint import pprint
import chromadb

with open('../sources.pickle', 'rb') as f:
    data = pickle.load(f)
    pprint(data)

with open('../db_cache.pickle', 'rb') as f:
    data = pickle.load(f)
    pprint(data)