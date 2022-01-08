from abc import abstractmethod

from modules.channel.domain.entities import Channel
from modules.shared_types.repository import GenericRepository


class ChannelRepository(GenericRepository):
    @abstractmethod
    def get_all(self, page_number: int, page_size: int, order_by: str) -> list[Channel]:
        ...


__all__ = (
    'ChannelRepository',
)
