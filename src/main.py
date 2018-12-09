import discord
import asyncio

client = discord.Client()

# On connection, output bot name to console
@client.event
async def on_ready():
    print('Logged in as')
    print(client.user.name)
    print(client.user.id)
    print('------')
    
    # Change "Playing" text
    await client.change_presence(game=discord.Game(name='with myself'))

@client.event
async def on_message(message):
    # Exits the bot iff I send the shutdown command
    if message.content.startswith('^quit') and message.author.id == '92305780048420864':
        tmp = await client.send_message(message.channel, "I am quitting")
        print("I am quitting because of channel command")
        await client.logout()
        quit()
    #Demo code from discord.py retained for now as reference
    '''
    elif message.content.startswith('^test'):
        counter = 0
        tmp = await client.send_message(message.channel, 'Calculating messages...')
        async for log in client.logs_from(message.channel, limit=100):
            if log.author == message.author:
                counter += 1

        await client.edit_message(tmp, 'You have {} messages.'.format(counter))
    elif message.content.startswith('^sleep'):
        await asyncio.sleep(5)
        await client.send_message(message.channel, 'Done sleeping')
    '''
client.run('!!!TOKEN!!!')