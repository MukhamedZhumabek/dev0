import asyncio
from logging import getLogger

from core.consumer import listen

logger = getLogger(__name__)

if __name__ == "__main__":
    logger.info("Start DEV0 service...")
    asyncio.run(listen())