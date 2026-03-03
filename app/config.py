from pydantic_settings import BaseSettings
from typing import Optional
import os
from dotenv import load_dotenv

class Settings(BaseSettings):
    debug: bool = False  # Add this field if missing

    # REDIS_HOST: str = "104.248.150.195"
    # REDIS_PORT:int = 6379
    # REDIS_PASSWORD: str = "KldkhhmS392"
    # REDIS_DB:int = 0

    # MONGO_USERNAME:str = 'admin'
    # MONGO_PASSWORD:str = 'KldkhhmS%23392'
    # MONGO_HOST:str = '143.198.201.33'
    # MONGO_PORT:int = 27017
    # MONGO_AUTH_SOURCE:str = 'admin'

    REDIS_HOST: str = os.getenv("REDIS_HOST","104.248.150.195")
    REDIS_PORT:int = os.getenv("REDIS_PORT",6379)
    REDIS_PASSWORD: str = os.getenv("REDIS_PASSWORD","KldkhhmS392")
    REDIS_DB:int = os.getenv("REDIS_DB",0)

    MONGO_USERNAME:str = os.getenv("MONGO_USERNAME",'admin')
    MONGO_PASSWORD:str = os.getenv("MONGO_PASSWORD",'KldkhhmS%23392')
    MONGO_HOST:str = os.getenv("MONGO_HOST",'143.198.201.33')
    MONGO_PORT:int = os.getenv("MONGO_PORT",27017)
    MONGO_AUTH_SOURCE:str = os.getenv("MONGO_AUTH_SOURCE",'admin')
    
    # MONGO_USERNAME: Optional[str] = None
    # MONGO_PASSWORD: Optional[str] = None
    # MONGO_HOST: str = "host.docker.internal"
    # MONGO_PORT: int = 27017
    # MONGO_AUTH_SOURCE: Optional[str] = None
    class Config:
        env_file = ".env"

settings = Settings()