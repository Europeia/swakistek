import logging
from string import Template

import discord
from discord.ext import commands

logger = logging.getLogger("swak")
logger.setLevel(logging.DEBUG)


class Bot(commands.Bot):
    def __init__(self, welcome_channel_id: int, welcome_message: Template):
        self._welcome_channel = None
        self._welcome_channel_id = welcome_channel_id
        self._welcome_message = welcome_message

        intents = discord.Intents.default()
        intents.members = True

        super().__init__(command_prefix=".", intents=intents,
                         allowed_mentions=discord.AllowedMentions(everyone=False, roles=False, users=True))

    async def on_ready(self):
        logger.info(f"Logged in as {self.user}")

    async def setup_hook(self) -> None:
        self._welcome_channel = await self.fetch_channel(self._welcome_channel_id)

    async def on_member_join(self, member: discord.Member):
        await self._welcome_channel.send(self._welcome_message.substitute(member_id=member.id))
