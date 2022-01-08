from typing import Optional
from pydantic.types import UUID4
from modules.channel.domain.repository import ChannelRepository
from modules.channel.infrastructure.models import Channels, Rates
from modules.channel.domain.entities import COUNT_RATES, Channel


class ChannelRepositoryDB(ChannelRepository):
    def __init__(self, db) -> None:
        self.db = db
    

    async def insert(self, channel: Channel) -> Channel:
        channel_db = Channels(**channel.dict(exclude={'rates'}))
        channel_db = await channel_db.save()
        return channel


    async def get_by_id(self, id: UUID4) -> Optional[Channel]:
        channel: Channels = await Channels.objects.get_or_none(id=id)
        if not channel:
            return None
        rates = await channel.rates.fields('rate') \
                     .order_by(Rates.id.desc()) \
                     .limit(COUNT_RATES) \
                     .values_list(fields='rate', flatten=True)
        return Channel(**channel.dict(exclude={'rates'}), rates=rates)
    

    async def get_all(self, page: int, page_size: int, order_by: str) -> list[Channel]:
        channels = await Channels.objects.select_related(Channels.rates) \
            .order_by([Channels.added_at.desc(), Channels.rates.id.desc()]) \
            .paginate(page, page_size).all()
        return [Channel(**row.dict(exclude={'rates'}),
                rates=[rate.rate for rate in row.rates[:COUNT_RATES]])
                for row in channels]

    
    async def delete(self, entity: Channel) -> UUID4:
        ...


    async def update(self, entity: Channel) -> Channel:
        ...

