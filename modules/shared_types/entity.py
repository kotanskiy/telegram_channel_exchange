from abc import ABC
from uuid import uuid4
from pydantic import BaseModel
from pydantic.fields import Field
from pydantic.types import UUID4



class Entity(ABC, BaseModel):
    id: UUID4 = Field(default_factory=uuid4)


__all__ = (
    'Entity',
)
