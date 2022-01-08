from typing import Optional
from fastapi import APIRouter
from fastapi.param_functions import Depends, Query
from pydantic.types import UUID4, PositiveInt
from modules.channel.module import get_channel_service
from modules.channel.app.services import ChannelService
from modules.channel.app.models import ChannelCreate, ChannelRepresentation


channels_router = APIRouter(tags=['Channels'])


@channels_router.post('/', response_model=ChannelRepresentation)
async def create_channel(
        data: ChannelCreate,
        service: ChannelService = Depends(get_channel_service)
    ):
    return await service.create_channel(data)


@channels_router.get('/{channel_id}', response_model=ChannelRepresentation)
async def get_channel(
        channel_id: UUID4,
        service: ChannelService = Depends(get_channel_service)
    ):
    return await service.get_channel(channel_id)


@channels_router.get('/', response_model=list[ChannelRepresentation])
async def get_chanels(
        page_number: PositiveInt = Query(default=1),
        service: ChannelService = Depends(get_channel_service)
    ):
    return await service.get_channel_list(page_number)


__all__ = (
    'channels_router',
)
