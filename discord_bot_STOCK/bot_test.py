# -*- coding: utf-8 -*-
"""
Created on Wed Dec 22 22:50:03 2021

@author: tony
"""

#導入 Discord.py
import discord
import nest_asyncio
from discord.ext import commands
import json
import os

with open('setting.json','r', encoding='utf8') as jfile:
    jdata = json.load(jfile)
    
bot = commands.Bot(command_prefix='!')

nest_asyncio.apply()



#調用 event 函式庫
@bot.event
#當機器人完成啟動時
async def on_ready():
    nest_asyncio.apply()
    print('目前登入身份：', bot.user)
    game = discord.Game('土中')
    #discord.Status.<狀態>，可以是online,offline,idle,dnd,invisible
    await bot.change_presence(status=discord.Status.idle, activity=game)
   
@bot.command()
async def load(ctx, extension):
    bot.load_extension(F'cmds.{extension}')
    await ctx.send(F'Loaded {extension} done')

@bot.command()
async def unload(ctx, extension):
    bot.unload_extension(F'cmds.{extension}')
    await ctx.send(F'unload {extension} done')

@bot.command()
async def reload(ctx, extension):
    bot.reload_extension(F'cmds.{extension}')
    await ctx.send(F'reload {extension} done')

for filename in os.listdir('./cmds'):
    if filename.endswith('.py'):
        bot.load_extension(F'cmds.{filename[:-3]}')
        print(filename)

#bot.run(jdata['TOKEN']) #TOKEN 在剛剛 Discord Developer 那邊「BOT」頁面裡面
if __name__ == "__main__":
    #print("test")
    bot.run(jdata['TOKEN']) #TOKEN 在剛剛 Discord Developer 那邊「BOT」頁面裡面
    