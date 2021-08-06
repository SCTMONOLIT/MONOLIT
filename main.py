import asyncio
import logging
from itertools import cycle

import discord
from discord.ext import commands
from discord.ext.commands import Bot

import config

logging.basicConfig(format = u'%(filename)s [LINE:%(lineno)d] #%(levelname)-8s [%(asctime)s]  %(message)s',
                    level = logging.INFO)


intents = discord.Intents.all()

bot = Bot(command_prefix = '.', help_command = None, intents = intents)

async def change_status():
    await bot.wait_until_ready()
    msg = cycle(status)

    while not bot.is_closed():
        next_status = next(msg)
        await bot.change_presence(activity = discord.Game(next_status))
        await asyncio.sleep(5)

status = ['status 1', 'status 2', 'status 3']


bot.load_extension('cogs.exo')
bot.load_extension('cogs.answer')
bot.load_extension('cogs.on_ready')
bot.load_extension('event.new_member')

bot.loop.create_task(change_status())
bot.run(config.TOKEN)