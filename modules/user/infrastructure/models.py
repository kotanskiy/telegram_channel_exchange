from datetime import datetime

import ormar
from pydantic.types import UUID4

from db.base import BaseMeta


class Users(ormar.Model):
    class Meta(BaseMeta):
        tablename = 'users'
    
    id: UUID4 = ormar.UUID(primary_key=True)
    register_at: datetime = ormar.DateTime(nullable=False, index=True)
    username: str = ormar.String(max_length=128, nullable=False)


__all__ = (
    'Users',
)
