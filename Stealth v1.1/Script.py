import discord #Esse é o mais importante!
from discord.ext import commands #Esse também é, mas nem tanto.
#Precisamos desses módulo para que funcione o programa!

client = commands.Bot(command_prefix='st?')
extensions = ['cumprimento'] #Vai "carregar a cog" que está entre ''

@client.event #Ele cria um evento
async def on_ready(): #Quando ele estiver pronto.
	#Ele vai imprimir isso no console.
	#Daqui...
    print("\n Logado como: {0.user}.\n  -ID: {0.user.id}\n".format(client))
    print("\n  Desenvolvido por: github.com/NathanXG!! \n")
    #...até aqui!


if __name__ == '__main__': #Isso define a main.
    for extension in extensions:
        try:
            client.load_extension(extension)
        except Exception as error:
            print(f'[{extension}] não funcionou. [{error}]')

    #O token que estiver estre as '', será ligado.
    client.run('')
