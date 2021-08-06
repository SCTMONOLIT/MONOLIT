import logging

import discord
from discord.ext import commands

class BotReady(commands.Cog):
    def __init__(self, bot: commands.Bot):
        super().__init__()
        self.bot = bot

    @commands.Cog.listener()
    async def on_ready(self):
        try:
            user: discord.Member = self.bot.get_user(399851432221868033)
            await user.send(
                'Бот запустився\n'\
                f'ID {self.bot.user.id}\n'\
                f'Name {self.bot.user.name}\n'\
                'Дякуємо, що використовуєте нашого бота!'
            )
        except Exception as e:
            logging.exception(e)

def setup(bot: commands.Bot):
    bot.add_cog(BotReady(bot))