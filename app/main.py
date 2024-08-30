from fastapi import FastAPI, HTTPException
import redis

from app.models import FareRule

app = FastAPI()

# Connect to Redis
redis_client = redis.Redis(host='redis', port=6379, db=0)

@app.post("/farerule")
async def store_farerule(farerule: FareRule):
    try:
        # Store the farerule in Redis if it doesn't exist
        if not redis_client.exists(farerule.hash):
            redis_client.set(farerule.hash, farerule.response)
            return {"message": "Fare rule stored successfully", "hash": farerule.hash}
        else:
            raise HTTPException(status_code=500, detail="Fare rule already exists in cache")
    except Exception as e:
        raise HTTPException(status_code=500, detail=str(e))

@app.post("/check/farerule")
async def check_farerule(farerule: FareRule):
    try:
        # Check if the farerule exists in Redis
        if redis_client.exists(farerule.hash):
            stored_rule = redis_client.get(farerule.hash).decode('utf-8')
            return {"message": "Fare rule exists in cache", "response": stored_rule, "hash": farerule.hash,}
        else:
            raise HTTPException(status_code=404,detail="Fare rule not found")
    except Exception as e:
        raise HTTPException(status_code=500, detail=str(e))