
from pydantic import BaseModel

# Define the Pydantic models

class FareRule(BaseModel):
    hash: str
    response: str
