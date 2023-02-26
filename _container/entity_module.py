from injector import Module, singleton, provider

from entity import Entity
from entity_config import EntityConfig


class EntityModule(Module):
    @singleton
    @provider
    def provide_entity(self, config: EntityConfig) -> Entity:
        return Entity(config)

    @singleton
    @provider
    def provide_entity_config(self) -> EntityConfig:
        return EntityConfig("Hello World")
