from datetime import datetime
from typing import Optional
from pydantic import UUID4, PositiveInt
from pydantic.types import PositiveFloat, confloat, conint, constr

from modules.shared_types.dto import DTO


class ChannelCreate(DTO):
    name: constr(min_length=2, max_length=128)
    description: Optional[constr(max_length=255)] = None
    count_of_subscribers: conint(ge=1)
    language: Optional[constr(min_length=2, max_length=2)] = None


class ChannelUpdate(ChannelCreate):
    id: UUID4


class ChannelRepresentation(ChannelUpdate):
    added_at: datetime
    rate: Optional[confloat(ge=1, le=5)] = None


__all__ = (
    'ChannelCreate',
    'ChannelUpdate',
    'ChannelRepresentation',
)
