from utils.database import database


class PreferencesRepository:

    @staticmethod
    async def create(name: str):
        query = "INSERT INTO preferences(name) VALUES (:name)"
        values = {"name": name}
        await database.execute(query=query, values=values)

    @staticmethod
    async def preferences():
        query = "SELECT * from preferences"
        return await database.fetch_all(query=query)
