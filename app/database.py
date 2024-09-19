from motor.motor_asyncio import AsyncIOMotorClient
from .config import settings
import redis

# MONGO_DETAILS = "mongodb+srv://muhammedarshadm:QgZEv11DThwYkC1y@cluster0.mfwgw.mongodb.net/?retryWrites=true&w=majority&appName=Cluster0"  # Replace with your MongoDB URI
MONGO_DETAILS = f"mongodb://{settings.MONGO_USERNAME}:{settings.MONGO_PASSWORD}@{settings.MONGO_HOST}:{settings.MONGO_PORT}/admin?authSource={settings.MONGO_AUTH_SOURCE}"


redis_client = None
mongo_client = None
mongo_db = None
cache_collection = None

async def init_clients():
    global redis_client, mongo_client, mongo_db,cache_collection
    redis_client = redis.Redis(host='localhost', port=6379, db=0)
    mongo_client = AsyncIOMotorClient(MONGO_DETAILS)
    mongo_db = mongo_client.cache_log
    cache_collection = mongo_db.get_collection("fare_rule_cache") # MongoDB database
