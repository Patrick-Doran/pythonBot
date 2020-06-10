import logging
import os
import discord  # pylint: disable=import-error
from dotenv import load_dotenv  # pylint: disable=import-error

#Implements logging into application
logging.basicConfig(level=logging.INFO) #NOTE:bot takes more time to start up, disable for speedier startups

#Gather private info from env
load_dotenv()
token = os.getenv('Discord_Token')
server = os.getenv('Server_Name')

#A client interacts with the Discord API
client = discord.Client()

@client.event
async def on_ready(): #Activates once connection to Discord is established
    # for guild in client.guilds: #Iterates through all of the servers that the bot is connected to
    #     if guild.name == server:
    #         break #Leave as soon as server id is found
    
    #Print out name of bot and the server its on
    print('Loggin in as  {0.user}'.format(client))

@client.event
async def on_message(message): #upon hearing the call of ~
    if str(message.channel) == "bot-speak-🤖": #the bot will only respond to commands made in the appropriate channel  
        if message.author == client.user: #prevents recursion with self
            return
        if message.content.startswith('~hello'):
            await message.channel.send('Hello.')
        else:
            await message.channel.send('I do not know that one.')

client.run(token)
