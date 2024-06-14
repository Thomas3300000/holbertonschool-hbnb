import json
import os
from Persistence.IPersistenceManager import IPersistenceManager


class DataManager(IPersistenceManager):
    def __init__(self, storage_path="data_store.json"):
        self.storage_path = storage_path
        self.data_store = self._load_data()

    def _load_data(self):
        if os.path.exists(self.storage_path):
            with open(self.storage_path, 'r') as file:
                return json.load(file)
        return {}

    def _save_data(self):
        with open(self.storage_path, 'w') as file:
            json.dump(self.data_store, file)

    def save(self, entity):
        entity_type = type(entity).__name__
        entity_id = entity.get('id')
        if entity_type not in self.data_store:
            self.data_store[entity_type] = {}
        self.data_store[entity_type][entity_id] = entity
        self._save_data()

    def get(self, entity_id, entity_type):
        return self.data_store.get(entity_type, {}).get(entity_id)

    def update(self, entity):
        entity_type = type(entity).__name__
        entity_id = entity.get('id')
        if {
            entity_type in self.data_store and entity_id in
            self.data_store[entity_type]
        }:
            self.data_store[entity_type][entity_id] = entity
            self._save_data()

    def delete(self, entity_id, entity_type):
        if {
            entity_type in self.data_store and entity_id in
            self.data_store[entity_type]
        }:
            del self.data_store[entity_type][entity_id]
            self._save_data()
