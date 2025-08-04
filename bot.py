import discord
from discord.ext import commands
from config import BOT_TOKEN


intents = discord.Intents.default()
intents.message_content = True

bot = commands.Bot(command_prefix="!", intents=intents)


@bot.event
async def on_ready():
    print(f"We have logged in as {bot.user}")


@bot.command()
async def hello(ctx):
    await ctx.send(f"Hello, {ctx.author.display_name}!")


@bot.command()
async def hi(ctx):
    await ctx.send(f"Hi, {ctx.author.display_name}!")


@bot.command()
async def goodbye(ctx):
    await ctx.send(f"Goodbye, {ctx.author.display_name}!")


@bot.command()
async def ping(ctx):
    await ctx.send("Pong!")


bot.run(BOT_TOKEN)

