import discord
import os
from discord.ext import commands
from dotenv import load_dotenv
from server import run
import random

load_dotenv()

intents = discord.Intents.all()
bot = commands.Bot(command_prefix='.', intents=intents)

@bot.event
async def on_ready():
    print(f'We have logged in as {bot.user.name}')

@bot.command(aliases=["all"])
async def everyone(ctx):
    await ctx.send('@everyone IMPORTANT MUST READ THE MESSAGE ABOVE!!!')

@bot.command(aliases=["zh"])
async def zhi_heng(ctx):
    await ctx.send('<@907197547301462017> IMPORTANT MUST READ THE MESSAGE ABOVE!!!')

@bot.command(aliases=["jh"])
async def jing_heng(ctx):
    await ctx.send('<@494490865109303296> IMPORTANT MUST READ THE MESSAGE ABOVE!!!')

@bot.command(aliases=["xl"])
async def xiang_le(ctx):
    await ctx.send('<@980775717526732882> IMPORTANT MUST READ THE MESSAGE ABOVE!!!')

@bot.command(aliases=["dy"])
async def dylan(ctx):
    await ctx.send('<@821979905482817547> IMPORTANT MUST READ THE MESSAGE ABOVE!!!')

@bot.command(aliases=["je"])
async def jeff(ctx):
    await ctx.send('<@462165645946126337> IMPORTANT MUST READ THE MESSAGE ABOVE!!!')

@bot.command(aliases=["hl"])
async def hoon_lim(ctx):
    await ctx.send('<@713990768792174642> IMPORTANT MUST READ THE MESSAGE ABOVE!!!')

@bot.command(aliases=["jy"])
async def jay_yong(ctx):
    await ctx.send('<@625819121979752450> IMPORTANT MUST READ THE MESSAGE ABOVE!!!')

@bot.event
async def on_message(message):
    if message.author == bot.user:
        return

    if message.content.startswith('<@1152087415587078215> who are you'):
        await message.channel.send('I am <@1152087415587078215> dumb dumb and I have random funny shitty command.')
        return
    
    if message.content.startswith('<@1152087415587078215> what command do you have'):
        await message.channel.send('''
                                   # List of fucking commands: 
                                   \n ## The . command 
                                   \n ### ping 
                                   \n jy/jh/zh/xl/dy/je/hl 
                                   \n all`@everyone`
                                   \n## The lolz command 
                                   \n\n\n### support 
                                   \n -<@1152087415587078215> who are you 
                                   \n -<@1152087415587078215> what command do you have
                                   ''')
        return
    
    await bot.process_commands(message)

    if message.content == '*canvas':
        for guild in bot.guilds:
            emojis = [discord.utils.get(guild.emojis, name='scream'),
                    discord.utils.get(guild.emojis, name='man_gesturing_no'),
                    discord.utils.get(guild.emojis, name='one'),
                    discord.utils.get(guild.emojis, name='regional_indicator_a'),
                    discord.utils.get(guild.emojis, name='regional_indicator_s'),
                    discord.utils.get(guild.emojis, name='regional_indicator_k')]
        print(emojis)
        #for emoji in emojis:
            #await message.add_reaction()

@bot.event
async def on_message_delete(message):
    if message.author.id == 1152087415587078215:
        author = ''
        channel = ''
    else:
        author =  f'{message.author.mention} : '
        channel = f' in **{message.channel}**'
    if len(message.content) > 1900:
        content = 'long....'
    else:
        content = message.content
    send_channel = bot.get_channel(1121687970227965952)
    await send_channel.send(f'{author} {content} {channel}')


# if __name__ == "__main__":
#     bot.run('')

if __name__ == "__main__":
    run()
    bot.run(os.getenv('DISCORD_TOKEN'))