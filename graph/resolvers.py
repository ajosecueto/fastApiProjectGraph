from typing import List

from models.preferences import Preference
from repository.preferences import PreferencesRepository


async def get_preferences() -> List[Preference]:
    results = await PreferencesRepository.preferences()
    return [Preference(name=result.name, created_at=result.created_at) for result in results]
