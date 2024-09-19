from app.models import FareRule
from .database import cache_collection,redis_client


async def get_from_redis(key):
    value = await redis_client.get(key)
    if value:
        return value.decode('utf-8')  # Convert bytes to string
    return None

# Function to check data in MongoDB
async def get_from_mongo(key):
    document = await cache_collection.find_one({"hash": key})
    if document:
        return document['response']
    return None


async def get_cache(key):
    # 1. Check Redis
    redis_data = await get_from_redis(key)
    if redis_data:
        return redis_data

    # 2. Check MongoDB if Redis missed
    mongo_data = await get_from_mongo(key)
    if mongo_data:
        return mongo_data

    # 3. If neither Redis nor MongoDB has the data, return False
    print(f"No data found for key: {key}")
    return False


async def store_to_redis(farerule:FareRule):
    redis_client.set(farerule.hash, farerule.response)

# Function to check data in MongoDB
async def store_to_mongo(farerule:FareRule):
    mongo_data = await get_from_mongo(farerule.hash)
    if not mongo_data:
        cache_collection.insert_one({'hash':farerule.hash,'response':farerule.response,"rule":farerule.rule})
    


async def store_cache(farerule:FareRule):
    await store_to_redis(farerule)
    await store_to_mongo(farerule)
    return True