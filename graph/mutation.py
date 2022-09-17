import json

import strawberry
from aiokafka import AIOKafkaProducer
from loguru import logger

from models.preferences import PreferenceInput
from utils.kafka import loop, KAFKA_BOOTSTRAP_SERVERS, KAFKA_TOPIC


@strawberry.type
class Mutation:
    @strawberry.mutation
    async def create_preferences(self, data: PreferenceInput) -> bool:
        producer = AIOKafkaProducer(loop=loop, bootstrap_servers=KAFKA_BOOTSTRAP_SERVERS)
        try:
            logger.info("Sending events")
            await producer.start()
            await producer.send_and_wait(topic=KAFKA_TOPIC, value=json.dumps({"name": data.name}).encode('utf-8'))
            return True
        except Exception as e:
            raise e
        finally:
            await producer.stop()
