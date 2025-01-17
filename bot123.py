import discord
from discord.ext import commands
import random
import requests

description = '''This is a basic bot i just hope it helps .

There are a number of utility commands being showcased here.'''

intents = discord.Intents.default()
intents.members = True
intents.message_content = True

bot = commands.Bot(command_prefix='?', description=description, intents=intents)

# Función para obtener la imagen del pato
def get_duck_image_url():    
    url = 'https://random-d.uk/api/random'
    res = requests.get(url)
    data = res.json()
    return data['url']

# Función para obtener la imagen del perro
def get_dog_image_url():
    url = 'https://random.dog/woof.json'
    res = requests.get(url)
    data = res.json()
    return data['url']

# Función para obtener la imagen del zorro
def get_fox_image_url():
    url = 'https://randomfox.ca/floof/'
    res = requests.get(url)
    data = res.json()
    return data['image']

@bot.command('duck')
async def duck(ctx):
    '''Una vez que llamamos al comando duck, el programa llama a la función get_duck_image_url'''
    image_url = get_duck_image_url()
    await ctx.send(image_url)

@bot.command('dog')
async def dog(ctx):
    '''Este comando devuelve una imagen aleatoria de un perro'''
    image_url = get_dog_image_url()
    await ctx.send(image_url)

@bot.command('fox')
async def fox(ctx):
    '''Este comando devuelve una imagen aleatoria de un zorro'''
    image_url = get_fox_image_url()
    await ctx.send(image_url)

@bot.event
async def on_ready():
    print(f'Logged in as {bot.user} (ID: {bot.user.id})')
    print('-----------')

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

@bot.command()
async def joined(ctx, member: discord.Member):
    """Says when a member joined."""
    await ctx.send(f'{member.name} pitifully he joined {discord.utils.format_dt(member.joined_at)}')

@bot.group()
async def nice(ctx):
    """Says if a user is nice."""
    if ctx.invoked_subcommand is None:
        await ctx.send(f'No, {ctx.subcommand_passed} you are wrong')

@bot.group()
async def cool(ctx):
    """For cool commands."""
    pass

@cool.command(name='bot')
async def _bot(ctx):
    """Is the bot amazing?"""
    await ctx.send('no')

bot.run('token')

