import discord
import asyncio
from discord.ext import commands

client = discord.Client()
id = client.get_guild('server_id')

inprog = 0
counter = 0
valid_channels = ['commands']

@client.event
async def on_ready():
    print('We have logged in as {0.user}'.format(client))

@client.event
async def on_message(message): #This event occurs everytime a message is sent in the guild
    if str(message.channel) == "commands":

        if message.content.startswith('$greetings'): #Command and automated response
            await message.channel.send('Hello {}!'.format(message.author.name))

        #Organize process by making it so that the message must be sent to the bot via a direct message
        #Only the original author of the command message may respond to the prompt

        if message.content.startswith('$repeat'):
            global inprog
            if inprog == 0:
                inprog = 1
                try:
                    msg = await message.author.send('Please respond with the phrase you would like me to repeat in **{}**:'.format(message.guild.name)) #Sends a direct message to the author of the command
                except discord.Forbidden: #In case of error
                    await message.author.send('Error')
                    inprog = 0
                    return

                def check(author):
                    def check2(message):
                        if message.author != author or message.channel != msg.channel:
                            return False
                        else:
                            return True
                    return check2

                try:
                    msg2 = await client.wait_for('message', check=check(message.author), timeout=30) #bot waits for a response from the author via direct message
                except asyncio.TimeoutError:
                    await message.author.send('You took too long!')
                    inprog = 0
                    return
                general = client.get_channel(712435402601922914)
                await general.send('@everyone')
                await general.send('```{} wants to announce:\n{}```'.format(message.author.name, msg2.content)) #posts the message in the chat
                inprog = 0
                
            else:
                await message.author.send('Someone is currently using the repeat command, please wait!')
        
        if message.content.startswith('$counter'):
            global counter
            counter = counter + 1
            await message.channel.send('```+1```')
        
        if message.content.startswith('$cdisplay'):
            await message.channel.send('```The counter is currently at: {}```'.format(counter))

        if message.content.startswith("$creset"):
            counter = 0
            await message.channel.send('```The counter has been reset.```')

        if message.content.startswith("$off"):
            await client.logout()

client.run('token')