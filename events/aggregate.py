import json

from aiokafka import AIOKafkaProducer
from loguru import logger

from utils.kafka import KAFKA_BOOTSTRAP_SERVERS, KAFKA_TOPIC_SEARCH, loop


async def add_search(value: dict) -> bool:
    producer = AIOKafkaProducer(loop=loop, bootstrap_servers=KAFKA_BOOTSTRAP_SERVERS)
    try:
        logger.info("Sending events")
        await producer.start()
        await producer.send_and_wait(topic=KAFKA_TOPIC_SEARCH, value=json.dumps(value).encode('utf-8'))
        return True
    except Exception as e:
        raise e
    finally:
        await producer.stop()
