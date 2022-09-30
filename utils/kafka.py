import asyncio

KAFKA_BOOTSTRAP_SERVERS = "localhost:9092"
KAFKA_TOPIC = "kafka"
KAFKA_TOPIC2 = "kafka2"
KAFKA_TOPIC_SEARCH = "kafka-search"
KAFKA_CONSUMER_GROUP = "group-id"
loop = asyncio.get_event_loop()
