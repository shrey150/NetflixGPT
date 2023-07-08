from os import path
import os
import shutil
import sys

try:
    from constants import *
except ModuleNotFoundError:
    sys.path.append(path.join(path.dirname(__file__), '..'))
    from constants import *

try:
    shutil.rmtree(DB_PATH)
    print(f"The folder '{DB_PATH}' has been deleted successfully.")
except OSError as e:
    print(f"Error: {e.filename} - {e.strerror}")

try:
    os.remove(CACHE_PATH)
    print(f"The file '{CACHE_PATH}' has been deleted successfully.")
except OSError as e:
    print(f"Error: {e.filename} - {e.strerror}")

try:
    os.remove(SOURCES_PATH)
    print(f"The file '{SOURCES_PATH}' has been deleted successfully.")
except OSError as e:
    print(f"Error: {e.filename} - {e.strerror}")

