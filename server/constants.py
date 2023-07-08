import os

BASE_DIR = os.path.dirname(__file__)
DOTENV_PATH = os.path.join(BASE_DIR, '../.env')

DB_PATH = os.path.join(BASE_DIR, 'db')
CACHE_PATH = os.path.join(BASE_DIR, 'db_cache.pickle')
SOURCES_PATH = os.path.join(BASE_DIR, 'sources.pickle')

PROMPT_REG_TXT_PATH = os.path.join(BASE_DIR, 'data/prompt.txt')
PROMPT_REG_JSON_PATH = os.path.join(BASE_DIR, 'data/prompt.txt')
PROMPT_QNA_TXT_PATH = os.path.join(BASE_DIR, 'data/qna.txt')
PROMPT_QNA_JSON_PATH = os.path.join(BASE_DIR, 'data/qna.json')
