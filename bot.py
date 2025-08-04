import discord
from config import BOT_TOKEN
import handle_client

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

    if message.content[0] == '!':
        try:
            response_pkt = handle_client.get_response(message)
            await message.channel.send(response_pkt)
        except ValueError:
            response_pkt = "No such command exists"
            print(response_pkt)
            await message.channel.send(response_pkt)
        except Exception as e:
            print(f"[on_message] Error occured: {e}")


client.run(BOT_TOKEN)

