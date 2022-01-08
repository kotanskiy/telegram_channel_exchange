from abc import ABC, abstractmethod

from modules.shared_types.entity import Entity


class GenericRepository(ABC):
    @abstractmethod
    def get_by_id(self, id: str | int) -> Entity:
        ...
    

    @abstractmethod
    def insert(self, entity: Entity) -> Entity:
        ...
    

    @abstractmethod
    def update(self, entity: Entity) -> Entity:
        ...
    

    @abstractmethod
    def delete(self, entity: Entity):
        ...


__all__ = (
    'GenericRepository',
)
