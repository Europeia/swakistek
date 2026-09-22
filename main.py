import logging
import os

from src.bot import Bot
from src.config import Config

logger = logging.getLogger("swak")
handler = logging.StreamHandler()
handler.setLevel(logging.DEBUG)
logger.addHandler(handler)


def main():
    config = Config.from_yaml(os.getenv("SWAK_CONFIG_FILE"))

    bot = Bot(
        config.welcome_channel_id,
        config.welcome_message,
        config.masked_role_id,
        config.masked_channel_id,
        config.masked_message,
    )

    bot.run(config.bot_token, log_handler=None)


if __name__ == "__main__":
    main()
