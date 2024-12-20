import os

from dotenv import load_dotenv
from pydantic import BaseConfig

load_dotenv()


class GlobalConfig(BaseConfig):
    title: str = os.environ.get("TITLE")
    version: str = "1.0.0"
    description: str = os.environ.get("DESCRIPTION")
    openapi_prefix: str = os.environ.get("OPENAPI_PREFIX")
    docs_url: str = "/docs"
    redoc_url: str = "/redoc"
    openapi_url: str = "/openapi.json"
    api_prefix: str = "/api"
    hash_length: int = int(os.environ.get("HASH_LENGTH"))
    mongo_connection: str = os.environ.get("MONGO_CONNECTION")
    redis_server: str = os.environ.get("REDIS_SERVER")
    redis_port: int = int(os.environ.get("REDIS_PORT"))


settings = GlobalConfig()
