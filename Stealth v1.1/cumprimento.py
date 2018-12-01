import discord #Esse é o mais importante!
from discord.ext import commands #Esse também é, mas nem tanto.
#Precisamos desses módulo para que funcione o programa!

class Eventos:
    def __init__(self, client):
        self.client = client

    #Evento on_message
    async def on_message(self, message): #A cada mensagem, ele vai analisar.
        if not message.author.bot: #Se a mensagem não for de um bot.
            for falas in ["oi", "olá", "oe", "iai", "eae", "ola"]:
                #Se o conteudo da mensagem, jogado pra minusculo, tiver algo da lista.
                if falas in message.content.lower():
                    #Ele vai respoder com <Olá (quem digitou)!!>
                    await message.channel.send(f"Olá {message.author.mention}!!")

def setup(client):
    client.add_cog(Eventos(client)) #Adicionamos essa cog na main.
