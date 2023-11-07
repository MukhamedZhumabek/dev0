import asyncio
import json
from logging import getLogger

from aio_pika import connect
from aio_pika.abc import AbstractIncomingMessage

import settings
from core.check_sum import check_sum
from core.publisher import publish

logger = getLogger(__name__)


async def on_message(message: AbstractIncomingMessage) -> None:
    body: dict[str, str] = json.loads(message.body)
    logger.info(f'Got message: {body}')
    if check_sum(data=body):
        await publish(settings.RABBITMQ_PUBLISH_QUEUE, message.body)


async def listen() -> None:
    connection = await connect(settings.RABBITMQ_URL)
    async with connection:
        channel = await connection.channel()
        queue = await channel.declare_queue("first")
        await queue.consume(on_message, no_ack=True)
        logger.info("Consumer waiting for messages...")
        await asyncio.Future()