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
    

intents = discord.Intents.default()
intents.message_content = True
client = discord.Client(intents=intents)

nest_asyncio.apply()
#client 是我們與 Discord 連結的橋樑


#調用 event 函式庫
@client.event
#當機器人完成啟動時
async def on_ready():
    nest_asyncio.apply()
    print('目前登入身份：', client.user)
    game = discord.Game('土中')
    #discord.Status.<狀態>，可以是online,offline,idle,dnd,invisible
    await client.change_presence(status=discord.Status.idle, activity=game)
    
@client.event   
async def on_message(msg):
    print("=======")
    print(msg)
    if msg.author == client.user:
        return   
    else:  
        for i in range(len(msg.content) - 2):
            if msg.content[i].lower() == ("l") and msg.content[(i + 1)].lower() == ("o") and msg.content[(i + 2)].lower() == ("l"):
                await msg.channel.send('打lol')
                break

        
        if msg.content == '1234':
            await msg.channel.send('5678')
'''  
@client.command()
async def load(ctx, extension):
    client.load_extension(F'cmds.{extension}')
    await ctx.send(F'Loaded {extension} done')

@client.command()
async def unload(ctx, extension):
    client.unload_extension(F'cmds.{extension}')
    await ctx.send(F'unload {extension} done')

@client.command()
async def reload(ctx, extension):
    client.reload_extension(F'cmds.{extension}')
    await ctx.send(F'reload {extension} done')

for filename in os.listdir('./cmds'):
    if filename.endswith('.py'):
        client.load_extension(F'cmds.{filename[:-3]}')
        print(filename)
'''
#bot.run(jdata['TOKEN']) #TOKEN 在剛剛 Discord Developer 那邊「BOT」頁面裡面
if __name__ == "__main__":
    #print("test")
    client.run(jdata['TOKEN']) #TOKEN 在剛剛 Discord Developer 那邊「BOT」頁面裡面
    