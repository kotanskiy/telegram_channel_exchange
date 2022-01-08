from abc import ABC
from pydantic import BaseModel



class ValueObject(ABC, BaseModel):
    class Config:
        allow_mutation = False



__all__ = (
    'ValueObject',
)
