import strawberry

from repository.preferences import PreferencesRepository


@strawberry.type
class Mutation:
    @strawberry.mutation
    async def create_preferences(self, name: str) -> bool:
        await PreferencesRepository.create(name=name)
        return True
