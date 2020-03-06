import os
import discord
from dotenv import load_dotenv

load_dotenv();
token = os.getenv('Discord_Token')
server = os.getenv('Server_Token')

client = discord.Client()

@client.event
async def on_ready():
    for guild in client.guilds:
        if guild.name == server:
            break

    print(f'{client.user} is connected to the server: ' f'{guild.name} id: {guild.id}')

client.run(token)
