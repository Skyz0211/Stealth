import discord
from discord.ext import commands

client = commands.Bot(command_prefix=[''])
initial_extensions = ['']

@client.event
async def on_ready():
    print("\n  Nenhum erro por enquanto... \n")
    print(" Logado como: {0.user}.\n  -ID: {0.user.id}\n".format(client))
    print("\n  Developers: github.com/NathanXG & github.com/!")
    while True:
        await client.change_presence(activity=discord.Streaming(name="Olá! digite m?ajuda",url="https://www.twitch.tv/bot_tutorial"))
        await asyncio.sleep(10)
        await client.change_presence(activity=discord.Streaming(name="github.com/NathanXG & github.com/!!",url="https://www.twitch.tv/bot_tutorial"))
        await asyncio.sleep(3)
        
client.run('')
