import discord
from discord.ext import commands
import asyncio
import random
import os
from dotenv import load_dotenv

load_dotenv()
TOKEN = os.getenv('DISCORD_TOKEN')

bot = commands.Bot(command_prefix='$')

antwortenW = ['1.e4', '1.d4', '1.c4', '1.Sf3', '1.b3', '1.f4', 'London']
antwortenS = ['Sizilianisch', 'Pirc', 'Skandinavisch', 'Aljechin', 'Caro-Kann', 'Französisch', 'Woher soll ich das wissen?']


# Login
@bot.event
async def on_ready():
    print('Status: SKYnet is ready')
    bot.loop.create_task(status_task())


# Welcome Message
@bot.event
async def on_member_join(member):
    await member.send(f'Hey {member.mention}, thanks for joining {member.guild.name}!')


@bot.command(pass_contest=True)
async def skynet(ctx):
    embed = discord.Embed(
        title='Befehle für SKYnet',
        description='Mit diesen Befehlen kannst du SKYnet steuern',
        colour=discord.Colour.red()
    )
    embed.add_field(name='`$slap`', value='Oldschool IRC slap', inline=True)
    embed.add_field(name='`$troutslap`', value='Prillwoods trout slap', inline=True)
    embed.add_field(name='`$lukas`', value='Nachwuchs!', inline=True)
    embed.add_field(name='`$carina`', value='Frowen', inline=True)
    embed.add_field(name='`$krieg`', value='Kampf', inline=True)
    embed.add_field(name='`$gambit`', value='Opfer!', inline=True)
    embed.add_field(name='`$ill`', value='krank?', inline=True)
    embed.add_field(name='`$ai`', value='wahre Intention', inline=True)
    embed.add_field(name='`$it`', value='Problemlösung', inline=True)
    embed.set_footer(text='--------------------------------------------------------------------------------')

    await ctx.send(embed=embed)


# -----------------------------------------------------------
# Statusmeldung anzeigen
async def status_task():
    while True:
        await bot.change_presence(activity=discord.Game(': Herzlich '), status=discord.Status.online)
        await asyncio.sleep(3)
        await bot.change_presence(activity=discord.Game(': Willkommen'), status=discord.Status.online)
        await asyncio.sleep(3)


# -----------------------------------------------------------

@bot.command()
async def lukas(ctx):
    await ctx.send('zukünftiger PYTHON.Coder und Weltmeisterschiedsrichter')


@bot.command()
async def krieg(ctx):
    await ctx.send('„Schach ist wie Krieg auf dem Brett. Das Ziel ist es, den Verstand seines Gegners zu brechen"')


@bot.command()
async def gambit(ctx):
    await ctx.send('„Du weißt, wie Schach gespielt wird. Figuren müssen geopfert werden!"')


@bot.command()
async def ill(ctx):
    await ctx.send('„Schach ist kein Spiel sondern eine Krankheit"')


@bot.command()
async def ai(ctx):
    await ctx.send(
        '$id = $_REQUEST[AI]; $result = mysql_query("SELFINJECT mach1n3 learning sk1llz from `skynet`"); result: **21%** - TAKING OVER WELTHERRSCHAFT')


@bot.command()
async def slap(ctx, members: commands.Greedy[discord.Member], *, reason='no reason'):
    slapped = ", ".join(x.name for x in members)
    await ctx.send(f'{slapped} just got slapped for {reason}')


@bot.command()
async def troutslap(ctx, members: commands.Greedy[discord.Member], *, reason='no reason'):
    slapped = ", ".join(x.name for x in members)
    await ctx.send('**Prillwood** slaps {} around a bit with a large trout'.format(slapped))


@bot.command()
async def carina(ctx):
    await ctx.send('**Carina**: „Man schlägt keine Frauen, nur Damen"')


@bot.command()
async def it(ctx):
    await ctx.send('„Ein neuer Boot macht alles gut!"')
# -----------------------------------------------------------

# 8ball
@bot.event
async def on_message(message):
    await bot.process_commands(message)
    if message.author.bot:
        return
    elif message.content.startswith('$8ball Weiß'):
        args = message.content.split(' ')
        if len(args) >= 2:
            frage = ' '.join(args[1:])
            mess = await message.channel.send('Intel i9-10850@**5,5**GHz verabeitet deine Frage:`{0}`'.format(frage))
            await asyncio.sleep(5)
            mess = await message.channel.send('Berechnung erfolgt')
            await asyncio.sleep(5)
            await mess.edit(content='Deine Antwort zur Frage:' ' `{0}` lautet: `{1}`'.format(frage, random.choice(antwortenW)))

    elif message.content.startswith('$8ball Schwarz'):
        args = message.content.split(' ')
        if len(args) >= 2:
            frage = ' '.join(args[1:])
            mess = await message.channel.send('Intel i9-10850@**5,5**GHz verabeitet deine Frage:`{0}`'.format(frage))
            await asyncio.sleep(5)
            mess = await message.channel.send('Berechnung erfolgt')
            await asyncio.sleep(5)
            await mess.edit(content='Deine Antwort zur Frage:' ' `{0}` lautet: `{1}`'.format(frage, random.choice(antwortenS)))


bot.run(os.getenv('TOKEN'))
