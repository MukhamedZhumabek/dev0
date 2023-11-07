from logging import getLogger

from aio_pika import Message, connect

import settings


logger = getLogger(__name__)


async def publish(queue_name: str, message: bytes) -> None:
    connection = await connect(settings.RABBITMQ_URL)
    async with connection:
        channel = await connection.channel()
        queue = await channel.declare_queue(queue_name)
        await channel.default_exchange.publish(
            Message(message),
            routing_key=queue.name,
        )
        logger.info(f'publish {message.decode("utf-8")}')

