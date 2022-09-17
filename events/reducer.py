import json

from aiokafka import AIOKafkaConsumer
from loguru import logger

from models.preferences import PreferenceInput
from repository.preferences import PreferencesRepository
from utils.kafka import loop, KAFKA_BOOTSTRAP_SERVERS, KAFKA_CONSUMER_GROUP, KAFKA_TOPIC


async def preferences_consumer():
    consumer = AIOKafkaConsumer(KAFKA_TOPIC, loop=loop,
                                bootstrap_servers=KAFKA_BOOTSTRAP_SERVERS, group_id=KAFKA_CONSUMER_GROUP)
    await consumer.start()
    try:
        async for msg in consumer:
            logger.info(f'Consumer msg: {msg}')
            data = PreferenceInput(**json.loads(msg.value))
            await PreferencesRepository.create(name=data.name)
    finally:
        await consumer.stop()
