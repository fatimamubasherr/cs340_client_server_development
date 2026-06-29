from pymongo import MongoClient


class AnimalShelter(object):
    """CRUD operations for the AAC animals collection."""

    def __init__(self, username, password):
        host = "localhost"
        port = 27017
        database = "aac"
        collection = "animals"

        self.client = MongoClient(
            f"mongodb://{username}:{password}@{host}:{port}/{database}?authSource=admin"
        )

        self.database = self.client[database]
        self.collection = self.database[collection]

    def create(self, data):
        if data is not None:
            try:
                result = self.collection.insert_one(data)
                return result.acknowledged
            except Exception as e:
                print("An error occurred during insert:", e)
                return False
        else:
            raise Exception("Nothing to save because data parameter is empty")

    def read(self, query):
        if query is not None:
            try:
                results = self.collection.find(query)
                return list(results)
            except Exception as e:
                print("An error occurred during read:", e)
                return []
        else:
            raise Exception("Nothing to search because query parameter is empty")

    def update(self, query, new_values):
        if query is not None:
            try:
                result = self.collection.update_many(query, new_values)
                return result.modified_count
            except Exception as e:
                print("An error occurred during update:", e)
                return 0
        else:
            raise Exception("Nothing to update because query parameter is empty")

    def delete(self, query):
        if query is not None:
            try:
                result = self.collection.delete_many(query)
                return result.deleted_count
            except Exception as e:
                print("An error occurred during delete:", e)
                return 0
        else:
            raise Exception("Nothing to delete because query parameter is empty")