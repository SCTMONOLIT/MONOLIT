import logging

import discord
from discord.ext import commands
from discord.ext.commands.context import Context
import random

class NewMember(commands.Cog):
    def __init__(self, bot: commands.Bot):
        super().__init__()
        self.bot = bot

    @commands.Cog.listener()
    async def on_member_join(self, member: discord.Member):
        try:
            r = random.randint(0, 225)
            g = random.randint(0, 225)
            b = random.randint(0, 225)


            emb = discord.Embed(
                title = 'Привіт!',
                description = f'Вітаємо на сервері {member.guild.name}',
                color = discord.Color.from_rgb(r, g, b),
                timestamp = member.joined_at
            )

            emb.set_thumbnail(
                url = member.avatar_url
            )

            emb.set_footer(
                text = f'{member.id} | Приятного времяпрепровождения!'
            )

            await self.bot.get_channel(805852513077035029).send(member.mention, embed = emb)

        except Exception as e:
            logging.exception(e)

def setup(bot: commands.Bot):
    bot.add_cog(NewMember(bot))