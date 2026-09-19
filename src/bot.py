import logging
from string import Template

import discord
from discord.ext import commands

logger = logging.getLogger("swak")
logger.setLevel(logging.DEBUG)


class Bot(commands.Bot):
    def __init__(
        self,
        welcome_channel_id: int | None,
        welcome_message: Template | None,
        masked_role_id: int | None = None,
        masked_channel_id: int | None = None,
        masked_message: Template | None = None,
    ):
        self._welcome_channel = None
        self._welcome_channel_id = welcome_channel_id
        self._welcome_message = welcome_message
        self._masked_role_id = masked_role_id
        self._masked_channel_id = masked_channel_id
        self._masked_message = masked_message

        intents = discord.Intents.default()
        intents.members = True

        super().__init__(
            command_prefix=".",
            intents=intents,
            allowed_mentions=discord.AllowedMentions(
                everyone=False, roles=False, users=True
            ),
        )

    async def on_ready(self):
        logger.info(f"Logged in as {self.user}")

    async def setup_hook(self) -> None:
        if self._welcome_channel_id and self._welcome_message:
            channel = await self.fetch_channel(self._welcome_channel_id)

            if isinstance(channel, discord.TextChannel):
                self._welcome_channel = channel
            else:
                logger.warning(
                    f"Channel with ID {self._welcome_channel_id} is not a text channel."
                )

        if self._masked_channel_id and self._masked_role_id and self._masked_message:
            channel = await self.fetch_channel(self._masked_channel_id)

            if isinstance(channel, discord.TextChannel):
                self._masked_channel = channel
            else:
                logger.warning(
                    f"Channel with ID {self._masked_channel_id} is not a text channel."
                )

    async def on_member_join(self, member: discord.Member):
        if self._welcome_channel and self._welcome_message:
            await self._welcome_channel.send(
                self._welcome_message.substitute(member_id=member.id)
            )

    async def on_member_update(self, before: discord.Member, after: discord.Member):
        if self._masked_channel and self._masked_role_id and self._masked_message:
            before_roles = {role.id for role in before.roles}
            after_roles = {role.id for role in after.roles}

            if (
                self._masked_role_id in after_roles
                and self._masked_role_id not in before_roles
            ):
                await self._masked_channel.send(
                    self._masked_message.substitute(member_id=after.id)
                )
