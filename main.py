import asyncio

import strawberry
from fastapi import FastAPI
from strawberry.fastapi import GraphQLRouter

from events.reducer import preferences_consumer
from graph.mutation import Mutation
from graph.query import Query
from utils.database import database

app = FastAPI()

schema = strawberry.Schema(Query, Mutation)

graphql_app = GraphQLRouter(schema)

app.include_router(graphql_app, prefix="/graphql")
asyncio.create_task(preferences_consumer())


@app.on_event("startup")
async def startup():
    await database.connect()


@app.on_event("shutdown")
async def shutdown():
    await database.disconnect()
