import os

from pydantic_settings import BaseSettings
from starlette.config import Config

current_file_dir = os.path.dirname(os.path.realpath(__file__))
env_path = os.path.join(current_file_dir, "..", ".env")
config = Config(env_path)

class PromptSettings(BaseSettings):
    PROMPT_REG_TXT_PATH: str = os.path.join(current_file_dir, 'data/prompt.txt')
    PROMPT_REG_JSON_PATH: str = os.path.join(current_file_dir, 'data/prompt.txt')
    PROMPT_QNA_TXT_PATH: str = os.path.join(current_file_dir, 'data/qna.txt')
    PROMPT_QNA_JSON_PATH: str = os.path.join(current_file_dir, 'data/qna.json')

# TODO remove all of these. we use Postgres now
class LegacySettings():
    DB_PATH: str = os.path.join(current_file_dir, 'db')
    CACHE_PATH: str = os.path.join(current_file_dir, 'db_cache.pickle')
    SOURCES_PATH: str = os.path.join(current_file_dir, 'sources.pickle')

class DatabaseSettings():
    DB_CONNECTION_URI = config("DB_CONNECTION_URI")

class Settings(
    PromptSettings,
    DatabaseSettings,
    LegacySettings,
):
    pass

settings = Settings()
