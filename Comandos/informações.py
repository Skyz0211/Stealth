import discord
import datetime
from discord.ext import commands 

class Informações:
    def __init__(self, client):
        self.client = client

    @commands.command()
    async def info(self, ctx):
    	Informacoes = discord.Embed(title="<:fakenews:504098432735248415> Informações", description="**`Em desenvolvimento...`** <:isaacyew:495719604799143936>")
    	await ctx.send(embed=Informacoes)

def setup(client):
    client.add_cog(Informações(client))