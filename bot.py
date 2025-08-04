import discord
from config import BOT_TOKEN

intents = discord.Intents.default()
intents.message_content = True

client = discord.Client(intents=intents)

@client.event
async def on_ready():
    print(f"We have logged in as {client.user}")

@client.event
async def on_message(message):
    if message.author == client.user:
        return

    if message.content.startswith('$hello'):
        response_pkt = f"hello {message.author.display_name}!"
        await message.channel.send(response_pkt)

client.run(BOT_TOKEN)

