from motor.motor_asyncio import AsyncIOMotorClient
from fastapi import FastAPI
import os
from .config import settings

# MONGO_DETAILS = "mongodb+srv://muhammedarshadm:QgZEv11DThwYkC1y@cluster0.mfwgw.mongodb.net/?retryWrites=true&w=majority&appName=Cluster0"  # Replace with your MongoDB URI
MONGO_DETAILS = f"mongodb://{settings.MONGO_USERNAME}:{settings.MONGO_PASSWORD}@{settings.MONGO_HOST}:{settings.MONGO_PORT}/admin?authSource={settings.MONGO_AUTH_SOURCE}"
client = AsyncIOMotorClient(MONGO_DETAILS)
database = client.cache_log
cache_collection = database.get_collection("fare_rule_cache")
