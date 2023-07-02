import os 
import shutil

BASE_DIR = os.path.dirname(__file__)
print("BASE")
db_folder = os.path.join(BASE_DIR, '../db')
db_pickle = os.path.join(BASE_DIR, '../db_cache.pickle')
sources_pickle = os.path.join(BASE_DIR, '../sources.pickle')

try:
    shutil.rmtree(db_folder)
    print(f"The folder '{db_folder}' has been deleted successfully.")
except OSError as e:
    print(f"Error: {e.filename} - {e.strerror}")

try:
    os.remove(db_pickle)
    print(f"The file '{db_pickle}' has been deleted successfully.")
except OSError as e:
    print(f"Error: {e.filename} - {e.strerror}")

try:
    os.remove(sources_pickle)
    print(f"The file '{sources_pickle}' has been deleted successfully.")
except OSError as e:
    print(f"Error: {e.filename} - {e.strerror}")

