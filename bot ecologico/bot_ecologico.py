import discord 
import random
from discord.ext import commands

#conf. do Bot
TOKEN = 'Aqui vai o meu token'

intents = discord.Intents.default()
intents.message_content = True

bot = commands.Bot(command_prefix='!', intents=intents)

##Base de dados simples para o bot
#lista
lixo_reciclavel = [
    'lata', 'saquinho', 'plasticos', 'jornais', 'papelão', 'envelopes', 'garrafa PET', 'latinhas de aluminio', 'tampinhas de garrafa', 'potes'
]

lixo_comum = [
    'fralda', 'resto de comida', 'cigarro', 'fio dental', 'papel higienico', 'papel sujo', 'algodão', 'espelho', 'escova de dente', 'pratos de plastico'
]

descarte_especial = [
    'pilha', 'remédio', 'curativos', 'agulhas', 'laminas', 'celulares', 'cabos', 'oleo de cozinha', 'lampadas fluorescentes'
]

@bot.command()
async def lixo(ctx, *, item=None):
    if item is None:
        await ctx.send('use assim: !lixo lata')
        return

    item = item.lower()

    if item in lixo_reciclavel:
        await ctx.send(f'{item} deve ir para a reciclagem.')

    elif item in lixo_comum:
        await ctx.send(f'{item} deve ir para o lixo comum.')

    else:
        await ctx.send(f'{item} esse item não existe ou nao foi digitado da forma certa, reescreva novamente.')

bot.run(TOKEN) 