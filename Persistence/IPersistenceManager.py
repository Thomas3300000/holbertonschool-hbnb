from abc import ABC, abstractmethod


class IPersistenceManager(ABC):
    @abstractmethod
    def save(self, entity):
        # Implementation to save the entity in storage
        pass

    @abstractmethod
    def get(self, entity_id, entity_type):
        # Implementation to retrieve an entity based on its ID and type
        pass

    @abstractmethod
    def update(self, entity):
        # Implementation for updating an entity in storage
        pass

    @abstractmethod
    def delete(self, entity_id, entity_type):
        # Implementation for deleting an entity from storage
        pass
