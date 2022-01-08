from datetime import datetime
from uuid import UUID
from fastapi.exceptions import HTTPException

from pydantic.error_wrappers import ValidationError
from modules.channel.domain.repository import ChannelRepository
from modules.channel.domain.entities import Channel
from modules.channel.app.models import ChannelCreate, ChannelRepresentation


PAGE_SIZE = 10


class ChannelService:
    def __init__(self, repo: ChannelRepository) -> None:
        self.repo = repo


    async def get_channel(self, id: UUID) -> ChannelRepresentation:
        channel: Channel = await self.repo.get_by_id(id)
        if not channel:
            raise HTTPException(404, f'Channel<{id}> not found')
        return ChannelRepresentation(**channel.dict())
    

    async def get_channel_list(self, page_number: int, order_by: str = '-added_at') -> list[ChannelRepresentation]:
        channels: list[Channel] = await self.repo.get_all(page_number, PAGE_SIZE, order_by)
        return [ChannelRepresentation(**channel.dict(exclude={'rates'})) for channel in channels]
    

    async def create_channel(self, data_model: ChannelCreate) -> ChannelRepresentation:
        try:
            channel = Channel(**data_model.dict(), added_at=datetime.now())
        except ValidationError as err:
            raise HTTPException(400, err.errors())
        channel: Channel = await self.repo.insert(channel)
        channel_representation = ChannelRepresentation(**channel.dict(exclude={'rates'}))
        return channel_representation
