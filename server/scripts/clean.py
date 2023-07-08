from os import path
import os
import shutil
import sys

try:
    from constants import DB_FOLDER, DB_PICKLE, SOURCES_PICKLE
except ModuleNotFoundError:
    sys.path.append(path.join(path.dirname(__file__), '..'))
    from constants import DB_FOLDER, DB_PICKLE, SOURCES_PICKLE

try:
    shutil.rmtree(DB_FOLDER)
    print(f"The folder '{DB_FOLDER}' has been deleted successfully.")
except OSError as e:
    print(f"Error: {e.filename} - {e.strerror}")

try:
    os.remove(DB_PICKLE)
    print(f"The file '{DB_PICKLE}' has been deleted successfully.")
except OSError as e:
    print(f"Error: {e.filename} - {e.strerror}")

try:
    os.remove(SOURCES_PICKLE)
    print(f"The file '{SOURCES_PICKLE}' has been deleted successfully.")
except OSError as e:
    print(f"Error: {e.filename} - {e.strerror}")

