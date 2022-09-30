import capnp

capnp.remove_import_hook()
preference_capnp = capnp.load('capnp/preference.capnp')
from aiokafka import AIOKafkaConsumer
from loguru import logger

from generated.proto import preferences_pb2
from repository.preferences import PreferencesRepository
from utils.kafka import loop, KAFKA_BOOTSTRAP_SERVERS, KAFKA_CONSUMER_GROUP, KAFKA_TOPIC, KAFKA_TOPIC2


async def preferences_consumer():
    consumer = AIOKafkaConsumer(*[KAFKA_TOPIC, KAFKA_TOPIC2], loop=loop,
                                bootstrap_servers=KAFKA_BOOTSTRAP_SERVERS, group_id=KAFKA_CONSUMER_GROUP)
    await consumer.start()
    try:
        async for msg in consumer:
            logger.info(f'Consumer msg: {msg}')
            if msg.topic == KAFKA_TOPIC:
                """
                  Protocol buffer
                """

                # preference = preferences_pb2.Preference()
                # preference.ParseFromString(msg.value)
                # logger.info(preference)
                # await PreferencesRepository.create(name=preference.name)

                """
                Capn'p Method
                """

                with preference_capnp.Preference.from_bytes(msg.value) as preference:
                    logger.info(preference)
                    await PreferencesRepository.create(name=preference.name)
            if msg.topic == KAFKA_TOPIC2:
                logger.info("Topic 2222222")

    finally:
        await consumer.stop()
