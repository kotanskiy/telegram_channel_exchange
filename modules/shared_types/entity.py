from abc import ABC
from uuid import uuid4
from pydantic import BaseModel
from pydantic.fields import Field
from pydantic.types import UUID4



class Entity(ABC, BaseModel):
    id: UUID4 = Field(default_factory=uuid4)


    @classmethod
    def get_properties(cls):
        return [prop for prop in dir(cls) if isinstance(getattr(cls, prop), property) and prop not in ("__values__", "fields")]


    def dict(self, *args, **kwargs) -> dict:
        attribs = super().dict(*args, **kwargs)
        props = self.get_properties()
        include, exclude = kwargs.get('include'), kwargs.get('exclude')
        if include:
            props = [prop for prop in props if prop in include]
        if exclude:
            props = [prop for prop in props if prop not in exclude]

        if props:
            attribs.update({prop: getattr(self, prop) for prop in props})

        return attribs


__all__ = (
    'Entity',
)
