from typing import List

import strawberry

from models.preferences import Preference
from graph.resolvers import get_preferences


@strawberry.type
class Query:
    preferences: List[Preference] = strawberry.field(resolver=get_preferences)