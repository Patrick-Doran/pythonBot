import discord
import asyncio
from discord.ext import commands

client = discord.Client()
id = client.get_guild('server_id')

inprog = 0

@client.event
async def on_ready():
    print('We have logged in as {0.user}'.format(client))

@client.event
async def on_message(message): #This event occurs everytime a message is sent in the guild

    if message.content.startswith('$greetings'): #Command and automated response
        await message.channel.send('Hello {}!'.format(message.author.name))

    def check(author):
        def check2(message):
            if message.author != author or message.channel != msg.channel:
                return False
            else:
                return True
        return check2

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
        
            try:
                msg2 = await client.wait_for('message', check=check(message.author), timeout=30) #bot waits for a response from the author via direct message
            except asyncio.TimeoutError:
                await message.author.send('You took too long!')
                inprog = 0
                return

            if len(msg2.content) != 0:
                await message.channel.send('```{} wants to announce:\n{}```'.format(message.author.name, msg2.content)) #posts the message in the chat
            inprog = 0
            
        else:
            await message.author.send('Someone is currently using the repeat command, please wait!')
        

#@bot.command(name='startpoll')
#async def create_poll(self, ctx):
#    try:
#        msg = await ctx.message.author.send("Please respond with the question you would like to pose in **{}**:".format(ctx.message.guild.name))
#    except discord.Forbidden:
#        await ctx.send("Fix yo shit.")
#        return

client.run('token')