from src.config import database


class DatabaseService:
    def __init__(self, collection: str):
        self.collection = collection

    @staticmethod
    async def save(collection: str, data: object) -> None:
        await database.get_collection(collection).insert_one(data)

    @staticmethod
    async def find_one(collection: str, query: object) -> object:
        return await database.get_collection(collection).find_one(query)
    
    @staticmethod
    def get_all(collection: str):
        return database.get_collection(collection).find()

    @staticmethod
    async def update_one(collection: str, query: object, update_values: object) -> None:
        await database.get_collection(collection).update_one(query, update_values)
