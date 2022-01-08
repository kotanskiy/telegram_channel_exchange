from abc import ABC
from pydantic import BaseModel


class DTO(ABC, BaseModel):
    class Config:
        allow_mutation = False


__all__ = (
    'DTO',
)
