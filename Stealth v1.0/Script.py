import discord #Esse é o mais importante!
from discord.ext import commands #Esse também é, mas nem tanto.
#Precisamos desses módulo para que funcione o programa!

client = commands.Bot(command_prefix='st?')

@client.event #Ele cria um evento
async def on_ready(): #Quando ele estiver pronto.
	#Ele vai imprimir isso no console.
	#Daqui...
    print("\n Logado como: {0.user}.\n  -ID: {0.user.id}\n".format(client))
    print("\n  Desenvolvido por: github.com/NathanXG!! \n")
    #...até aqui!

@client.event #Ele cria um evento.
async def on_message(message): #A cada mensagem, ele vai analisar.
    if not message.author.bot: #Se a mensagem não for de um bot.
        for falas in ["oi", "olá", "oe", "iai", "eae", "ola"]:
            #Se o conteudo da mensagem, jogado pra minusculo, tiver algo da lista.
            if falas in message.content.lower():
            	#Ele vai respoden com <Olá (quem digitou)!!>
                await message.channel.send(f"Olá {message.author.mention}!!")

#O token que estiver estre as '', será ligado.
client.run('')
