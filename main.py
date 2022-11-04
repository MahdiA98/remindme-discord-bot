import discord
from discord.ext import commands
from dotenv import load_dotenv
import os

load_dotenv()

intents = discord.Intents.all()
intents.members = True

bot = commands.Bot(command_prefix="!", intents=intents)

bot.command()
async def hello(ctx):
    await ctx.reply("Hello")

bot.run(os.getenv("TOKEN"))




