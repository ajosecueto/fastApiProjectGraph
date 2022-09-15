from datetime import datetime

import strawberry


@strawberry.type
class Preference:
    name: str
    created_at: datetime

