import capnp

capnp.remove_import_hook()
preference_capnp = capnp.load('capnp/preference.capnp')
import strawberry
from aiokafka import AIOKafkaProducer
from loguru import logger

from generated.proto import preferences_pb2 as preferences_pb2
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
            """
             Protocol buffer
             bytes 21
             """
            # preference = preferences_pb2.Preference(name=data.name)
            # logger.info(len(preference.SerializeToString()))
            # await producer.send_and_wait(topic=KAFKA_TOPIC, value=preference.SerializeToString())

            """
             Capn'p Method
             bytes 48
             """
            preference = preference_capnp.Preference.new_message()
            preference.name = data.name
            logger.info(len(preference.to_bytes()))
            await producer.send_and_wait(topic=KAFKA_TOPIC, value=preference.to_bytes())
            return True
        except Exception as e:
            raise e
        finally:
            await producer.stop()
