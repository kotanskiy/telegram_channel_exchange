from datetime import datetime
from typing import Optional

import ormar
from pydantic.types import UUID4

from db.base import BaseMeta
from modules.user.infrastructure.models import Users


class Channels(ormar.Model):
    class Meta(BaseMeta):
        tablename = 'channels'

    id: UUID4 = ormar.UUID(primary_key=True)
    added_at: datetime = ormar.DateTime(nullable=False, index=True)
    name: str = ormar.String(max_length=128, nullable=False)
    description: Optional[str] = ormar.String(max_length=255, nullable=True)
    count_of_subscribers: int = ormar.Integer(minimum=1, nullable=False)
    language: Optional[str] = ormar.String(min_length=2, max_length=2, nullable=True)
    



class Rates(ormar.Model):
    class Meta(BaseMeta):
        tablename = 'rates'
        constraints = [ormar.UniqueColumns('user_id', 'channel_id')]

    
    id: int = ormar.Integer(primary_key=True, autoincrement=True)
    user_id: Users = ormar.ForeignKey(Users, nullable=False, related_name='rates')
    channel_id: Channels = ormar.ForeignKey(Channels, nullable=False, related_name='rates')
    rate: int = ormar.SmallInteger(minimum=1, maximum=5, nullable=False)


__all__ = (
    'Channels',
    'Rates',
)
