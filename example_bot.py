import discord
from discord.ext import commands

client = discord.Client()
id = client.get_guild(#server_id)

@client.event
async def on_ready():
    print('We have logged in as {0.user}'.format(client))

@client.event
async def on_message(message): #This event occurs everytime a message is sent in the guild

    if message.content.startswith('$greetings'): #Command and automated response
        await message.channel.send('Hello {}!'.format(message.author.name))

    if message.content.startswith('$repeat'):
        try:
            msg = await message.author.send('Please respond with the phrase you would like me to repeat in **{}**:'.format(message.guild.name)) #Sends a direct message to the author of the command
        except discord.Forbidden: #In case of error
            await message.author.send('Error')
            return
        
        try:
            msg2 = await client.wait_for('message') #bot waits for a response from the author via direct message
        except discord.Forbidden:
            await message.author.send('Error2')
            return

        await message.channel.send('```{} wants to ask:\n{}```'.format(message.author.name, msg2.content)) #posts the message in the chat
        

#@bot.command(name='startpoll')
#async def create_poll(self, ctx):
#    try:
#        msg = await ctx.message.author.send("Please respond with the question you would like to pose in **{}**:".format(ctx.message.guild.name))
#    except discord.Forbidden:
#        await ctx.send("Fix yo shit.")
#        return

client.run(#token)