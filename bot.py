import os
import discord 
from dotenv import load_dotenv

#Gather private info
load_dotenv()
token = os.getenv('Discord_Token')
server = os.getenv('Server_Token')

#A client interacts with the Discord API
client = discord.Client()

@client.event
async def on_ready(): #Activates once connection to Discord is established
    for guild in client.guilds: #Iterates through all of the servers that the bot is connected to
        if guild.name == server:
            break #Leave as soon as server id is found
    #Print out name of bot and the server its on
    print(f'{client.user} is connected to the server: ' f'{guild.name} id: {guild.id} \n')

    #Print out all of the members in the server
    members = '\n - '.join([member.name for member in guild.members])
    print(f'Guild Members:\n - {members}')


client.run(token)
