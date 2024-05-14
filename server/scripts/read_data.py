import pickle
from pprint import pprint
# import chromadb
from os import path

BASE_DIR = path.dirname(__file__)

with open(path.join(BASE_DIR, '../sources.pickle'), 'rb') as f:
    data = pickle.load(f)
    pprint(data)

with open(path.join(BASE_DIR, '../db_cache.pickle'), 'rb') as f:
    data = pickle.load(f)
    pprint(data)