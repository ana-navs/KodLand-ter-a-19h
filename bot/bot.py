import discord
import os
import random
import requests
from discord.ext import commands

intents = discord.Intents.default()
intents.message_content = True

bot = commands.Bot(command_prefix='$', intents=intents)

@bot.event#é uma caracteristica pq tem apenas .
async def on_ready():
    print(f'Estamos logados como {bot.user}')

#area para funçoes

def get_duck_image_url():    
    url = 'https://random-d.uk/api/random'
    res = requests.get(url)
    data = res.json()
    return data['url']

#Comandos/açoes

@bot.command() #é uma funçao pq tem . e ()
async def hello(ctx):
    await ctx.send(f'Olá! eu sou um bot {bot.user}!')

@bot.command()
async def heh(ctx, count_heh = 5):
    await ctx.send("he" * count_heh)

@bot.command()
async def joined(ctx, member: discord.Member):
    # Mostra quando um membro específico entrou no servidor.
    data_formatada = member.joined_at.strftime("%d/%m/%Y")
    await ctx.send(f"Boas-vindas! O usuário {member.name} entrou no servidor no dia {data_formatada}.")

    # "O usuario " + usuario + " "
    # "O usuario", usuario, " "
    # f"O usuario {usuario} "

@bot.command()
async def meme(ctx):
    #pegar todos os arquivos dentro da pasta imagnens
    images = os.listdir('img')

    #escolher imagem aleatoria
    img_random = random.choice('images')

    #Abrir a imagem escolhida e enviar para o discord
    with open (f'img/{img_name}', 'rb') as f: 
        picture = discord.File(f)
        await ctx.send(file = picture)

@bot.command('duck')
async def duck(ctx):
    '''Uma vez que chamamos o comando duck, o programa chama a função get_duck_image_url '''
    image_url = get_duck_image_url()
    await ctx.send(image_url)

#tarefa:

@bot.command()
async def add(ctx, left: int, right: int):
    """Adds two numbers together."""
    await ctx.send(left + right)


@bot.command()
async def roll(ctx, dice: str):
    """Rolls a dice in NdN format."""
    try:
        rolls, limit = map(int, dice.split('d'))
    except Exception:
        await ctx.send('Format has to be in NdN!')
        return

    result = ', '.join(str(random.randint(1, limit)) for r in range(rolls))
    await ctx.send(result)


@bot.command(description='For when you wanna settle the score some other way')
async def choose(ctx, *choices: str):
    """Chooses between multiple choices."""
    await ctx.send(random.choice(choices))


@bot.command()
async def repeat(ctx, times: int, content='repeating...'):
    """Repeats a message multiple times."""
    for i in range(times):
        await ctx.send(content)


@bot.group()
async def cool(ctx):
    """Says if a user is cool.

    In reality this just checks if a subcommand is being invoked.
    """
    if ctx.invoked_subcommand is None:
        await ctx.send(f'No, {ctx.subcommand_passed} is not cool')


@cool.command(name='bot')
async def _bot(ctx):
    """Is the bot cool?"""
    await ctx.send('Yes, the bot is cool.')

bot.run("O TOKEN SECRETO FICA AQUI")
