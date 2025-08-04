#!.venv/bin/python3.12
import discord
from discord.ext import commands
from config import BOT_TOKEN
import json


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


@bot.command()
async def add(ctx, *args):
    try: 
        nums = [float(x) for x in args]
        ans = sum(nums)
        await ctx.send(ans)
    except:
        await ctx.send("addition allowed for numbers only")


#@bot.command()
#async def gitfetch(ctx, git_username, git_repo_name):
    #git_info = gitcord.fetch_gitinfo(git_username, git_repo_name)
    #username = git_info["user_name"]
    #repo = git_info["repository"]
    #commit_id = git_info["commit_id"]
    #last_commit_date = git_info["last_commit_date"]
    #await ctx.send(response)


bot.run(BOT_TOKEN)

