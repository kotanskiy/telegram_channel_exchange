from fastapi import Depends
from modules.channel.domain.repository import ChannelRepository
from modules.channel.infrastructure.repository import ChannelRepositoryDB
from modules.channel.app.services import ChannelService
from db.base import database


def get_channel_repository() -> ChannelRepository:
    return ChannelRepositoryDB(database)


def get_channel_service(repo: ChannelRepository = Depends(get_channel_repository)):
    return ChannelService(repo)
