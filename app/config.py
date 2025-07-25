from pydantic_settings import BaseSettings
from typing import Optional

class Settings(BaseSettings):
    debug: bool = False  # Add this field if missing

    REDIS_HOST: str = "178.128.58.228"
    REDIS_PORT:int = 6379
    REDIS_PASSWORD: str = "KldkhhmS392"
    REDIS_DB:int = 0

    # MONGO_USERNAME:str = 'admin'
    # MONGO_PASSWORD:str = 'KldkhhmS%23392'
    # MONGO_HOST:str = '206.189.91.84'
    # MONGO_PORT:int = 27017
    # MONGO_AUTH_SOURCE:str = 'admin'
    
    MONGO_USERNAME: Optional[str] = None
    MONGO_PASSWORD: Optional[str] = None
    MONGO_HOST: str = "host.docker.internal"
    MONGO_PORT: int = 27017
    MONGO_AUTH_SOURCE: Optional[str] = None
    class Config:
        env_file = ".env"

settings = Settings()