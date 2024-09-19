from contextlib import asynccontextmanager
from fastapi import FastAPI, HTTPException
from app.service import get_cache, store_cache
from app.models import FareRule
from .database import init_clients,redis_client

@asynccontextmanager
async def lifespan(app: FastAPI):
    await init_clients()
   
    try:
        yield
    finally:
        redis_client.close()
        await redis_client.wait_closed()


app = FastAPI(lifespan=lifespan)

@app.post("/farerule")
async def store_farerule(farerule: FareRule):
    try:
        data = await get_cache(farerule.hash)
        if data:
            return {"message": "Fare rule exists in cache", "response": data, "hash": farerule.hash,}
        else:
            if farerule.response is not None:
                await store_cache(farerule=farerule)
                return {"message": "Fare rule stored successfully","hash":farerule.hash}
        raise HTTPException(status_code=500, detail=str(e))
    except Exception as e:
        raise HTTPException(status_code=500, detail=str(e))