import os
import datetime
import discord
import asyncio
from dotenv import load_dotenv, find_dotenv
from discord.ext import commands
load_dotenv(find_dotenv())

discord.utils.setup_logging()
activity = discord.Activity(type=discord.ActivityType.listening, name="TWICE")
intents = discord.Intents.default()
intents.message_content = True  
bot = commands.Bot(command_prefix="ma$",intents=intents, activity=activity)

@bot.event
async def on_ready():
  print(f'Logged on as', {bot.user})
  synced = await bot.tree.sync()

async def load():
  for file in os.listdir('./cogs'):
    if file.endswith('.py'):
      await bot.load_extension(f'cogs.{file[:-3]}')

async def main():
  await load()
  await bot.start(os.getenv('TOKEN'))

#para recordarme el chino
# @bot.command(name="reminder", description="reminds you anything")
# async def remind(ctx, msg:str, day:int, hour:int, minute:int):
#   now = datetime.datetime.now()
#   then = now+datetime.timedelta(days=day)
#   then = now.replace(hour=hour, minute=minute)
#   delta = (then-now).total_seconds()
  
#   await ctx.send(f"{ctx.author.mention}\nI'll remind you: {msg} in {day} days, at {hour} hours and {minute} minutes")
#   await asyncio.sleep(delta)
  

#   await ctx.send(f" {ctx.author.mention}\nYou told me to remind: {msg}")

asyncio.run(main())