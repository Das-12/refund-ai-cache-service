from contextlib import asynccontextmanager
from fastapi import FastAPI, HTTPException
from app.service import get_cache, store_cache
from app.models import FareRule
from .database import init_clients, redis_client

# @asynccontextmanager
# async def lifespan(app: FastAPI):
#     await init_clients()
#     print("client initialised:",redis_client)
   
#     try:
#         yield
#     finally:
#         redis_client.close()
#         await redis_client.wait_closed()


# app = FastAPI(lifespan=lifespan)

# @app.post("/farerule")
# async def store_farerule(farerule: FareRule):
#     try:
#         data = await get_cache(farerule.hash)
#         if data:
#             return {"message": "Fare rule exists in cache", "response": data, "hash": farerule.hash,}
#         else:
#             if farerule.response is not None:
#                 await store_cache(farerule=farerule)
#                 return {"message": "Fare rule stored successfully","hash":farerule.hash}
#         raise HTTPException(status_code=500, detail=str(e))
#     except Exception as e:
#         raise HTTPException(status_code=500, detail=str(e))

import traceback
from fastapi import FastAPI, HTTPException
import redis
from .config import settings
from app.models import FareRule
from .database import cache_collection, mongo_client
from contextlib import asynccontextmanager

@asynccontextmanager
async def lifespan(app:FastAPI):
     await init_clients()
     print("cache collection:",cache_collection)
     yield
     mongo_client.close()


app = FastAPI(lifespan=lifespan)

# Connect to Redis
redis_client = redis.Redis(host=settings.REDIS_HOST, port=settings.REDIS_PORT, db=settings.REDIS_DB,password=settings.REDIS_PASSWORD)

@app.post("/farerule")
async def store_farerule(farerule: FareRule):
    # try:
    #     document = await cache_collection.find_one({'hash': farerule.hash})
    #     if document:
    #         if not redis_client.exists(farerule.hash):
    #             redis_client.set(farerule.hash, farerule.response)
    #             return {"message": "Fare rule stored successfully", "hash": farerule.hash}
    #         else:
    #             raise HTTPException(status_code=500, detail="Fare rule already exists in cache")
    #     else:
    #         cache_collection.insert_one({'hash':farerule.hash,'response':farerule.response})
    #         if not redis_client.exists(farerule.hash):
    #             redis_client.set(farerule.hash, farerule.response)
    #             return {"message": "Fare rule stored successfully", "hash": farerule.hash}
    #         else:
    #             raise HTTPException(status_code=500, detail="Fare rule already exists in cache")
    #     # Store the farerule in Redis if it doesn't exist
        
    # except Exception as e:
    #     raise HTTPException(status_code=500, detail=str(e))
    if cache_collection is None:
         print("Cache collection is None!", cache_collection)
    document = await cache_collection.find_one({'hash': farerule.hash})
    if document:
            if not redis_client.exists(farerule.hash):
                redis_client.set(farerule.hash, farerule.response)
                return {"message": "Fare rule stored successfully", "hash": farerule.hash}
            # else:
            #     raise HTTPException(status_code=500, detail="Fare rule already exists in cache")
    else:
            cache_collection.insert_one({'hash':farerule.hash,'response':farerule.response})
            if not redis_client.exists(farerule.hash):
                redis_client.set(farerule.hash, farerule.response)
                return {"message": "Fare rule stored successfully", "hash": farerule.hash}
            else:
                # raise HTTPException(status_code=500, detail="Fare rule already exists in cache")
                print("already exists..!!!")

@app.post("/check/farerule")
async def check_farerule(farerule: FareRule):
    try:
        # Check if the farerule exists in Redis
        if redis_client.exists(farerule.hash):
            print("fare rule exists in redis.")
            stored_rule = redis_client.get(farerule.hash).decode('utf-8')
            return {"message": "Fare rule exists in cache", "response": stored_rule, "hash": farerule.hash,}
        else:
            document = await cache_collection.find_one({'hash': farerule.hash})
            if document:
                redis_client.set(farerule.hash, document['response'])
                return {"message": "Fare rule exists in cache", "response": document['response'], "hash": farerule.hash,}
            else:
                raise HTTPException(status_code=404,detail="Fare rule not found")
    except Exception as e:
        print(traceback.format_exc())
        raise HTTPException(status_code=500, detail=str(e))
    
