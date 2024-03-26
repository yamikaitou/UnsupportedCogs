import logging
from typing import Literal, Optional

import discord
from redbot.core import app_commands, commands
from redbot.core.bot import Red
from redbot.core.config import Config

log = logging.getLogger("red.yamicogs.talk")

RequestType = Literal["discord_deleted_user", "owner", "user", "user_strict"]


class PRBankEvents(commands.Cog):
    """Testing for PR 5325"""

    def __init__(self, bot: Red) -> None:
        self.bot = bot

    @commands.Cog.listener()
    async def on_red_bank_set_global(self, state):
        await self.bot.get_channel(888531685975674890).send(f"[set_global] {state}")

    @commands.Cog.listener()
    async def on_red_bank_set_balance(self, payload):
        await self.bot.get_channel(888531685975674890).send(f"[set_balance] {payload.recipient_id} in {payload.guild_id}, old {payload.recipient_old_balance}, new {payload.recipient_new_balance}")

    @commands.Cog.listener()
    async def on_red_bank_transfer_credits(self, payload):
        await self.bot.get_channel(888531685975674890).send(f"[transfer_credits] in {payload.guild_id}, {payload.sender_id} ({payload.sender_new_balance}) sent {payload.transfer_amount} to {payload.recipient_id} ({payload.recipient_new_balance})")

    @commands.Cog.listener()
    async def on_red_bank_wipe(self, guild_id):
        await self.bot.get_channel(888531685975674890).send(f"[bank_wipe] {guild_id}")

    @commands.Cog.listener()
    async def on_red_bank_prune_accounts(self, payload):
        await self.bot.get_channel(888531685975674890).send(f"[prune_accounts] {scope}, {pruned_users}")
    