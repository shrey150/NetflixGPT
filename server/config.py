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
    DB_CONNECTION_URI: str = config("DB_CONNECTION_URI")

class PineconeSettings():
    PINECONE_API_KEY: str = config("PINECONE_API_KEY")

class RedisQueueSettings():
    REDIS_QUEUE_HOST: str = config("REDIS_QUEUE_HOST", default="localhost")
    REDIS_QUEUE_PORT: int = config("REDIS_QUEUE_PORT", default=6379)
    REDIS_QUEUE_DB: int = config("REDIS_QUEUE_DB", default=0)
    REDIS_QUEUE_URI: str = f"redis://{REDIS_QUEUE_HOST}:{REDIS_QUEUE_PORT}/{REDIS_QUEUE_DB}"

class OpenAISettings():
    OPENAI_API_KEY: str = config("OPENAI_API_KEY")

class Settings(
    PromptSettings,
    DatabaseSettings,
    LegacySettings,
    RedisQueueSettings,
    OpenAISettings,
    PineconeSettings,
):
    pass

settings = Settings()
