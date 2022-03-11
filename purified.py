import discord
from discord.ext import commands
import datetime as dt
import asyncio
import json
import os


intents = discord.Intents().all()
bot = commands.Bot(command_prefix='=', intents=intents)
bot.remove_command('help')
    
with open('setting.json', 'r', encoding='utf8')as jFile:
    data=json.load(jFile)





@bot.event
async def on_ready():
    print('目前登入身份：', bot.user)
    channel = bot.get_channel(int(data["ready_channel"]))
    await bot.change_presence(status=discord.Status.online, activity=discord.Activity(type=discord.ActivityType.watching, name='over us'))
    await channel.send('貴安，大家深愛的天使Purified啟動成功!')

@bot.event
async def on_disconnect():
    channel = bot.get_channel(int(data["ready_channel"]))
    broken=rd.radiant(1,10)
    await channel.send('@877361885236850718'+'機器人壞掉啦!!!')
    if broken==8:
        await channel.send('不-不行，要壞掉了')
    else:
        await channel.send('突然...好困...')

@bot.command()
async def help(ctx):
    time_del = dt.timedelta(hours=8)
    new_dt = dt.datetime.now()- time_del
    embed=discord.Embed(
    title="Here's the command list~",
    color=0x90dff9,
    timestamp = new_dt
    )
    embed.add_field(
    name="Utility",
    value="help, ping",
    inline=True
    )
    embed.add_field(
    name="fun",
    value="say",
    inline=True)
    await ctx.send(embed=embed)

@bot.command()
async def load(ctx, extension):
    bot.load_extension(F"cmds.{extension}")
    await ctx.send(F"{extension}加載完成！")

@bot.command()
async def unload(ctx, extension):
    bot.unload_extension(F"cmds.{extension}")
    await ctx.send(F"{extension}卸載完成！")

@bot.command()
async def reload(ctx, extension):
    bot.reload_extension(F"cmds.{extension}")
    await ctx.send(F"{extension}重啟完成！")

for filename in os.listdir("./cmds"):
    if filename.endswith(".py"):
        bot.load_extension(F"cmds.{filename[:-3]}")










if __name__=="__main__":
    bot.run(data["token"])
