from injector import Injector

from _container.entity_module import EntityModule
from entity import Entity

injector = Injector([EntityModule()])
print(injector.get(Entity).config.name)
