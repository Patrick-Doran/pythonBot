import os
import discord 
from dotenv import load_dotenv

#Gather private info from env
load_dotenv()
token = os.getenv('Discord_Token')
server = os.getenv('Server_Token')

#A client interacts with the Discord API
client = discord.Client()

@client.event
async def on_ready(): #Activates once connection to Discord is established
    # for guild in client.guilds: #Iterates through all of the servers that the bot is connected to
    #     if guild.name == server:
    #         break #Leave as soon as server id is found
    #Print out name of bot and the server its on
    print('Loggin in as  {0.user}'.format(client)) #Prints name in terminal

@client.event
async def on_message(message): #upon hearing the call of ~
    if message.author == client.user: #prevents recursion with self
        return
    if message.content.startswith('~hello'):
        await message.channel.send('Hello.')

client.run(token)
