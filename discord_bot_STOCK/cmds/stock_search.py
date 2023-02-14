# -*- coding: utf-8 -*-
"""
Created on Mon Dec 27 16:33:58 2021

@author: ailab05
"""

import discord
import nest_asyncio
from discord.ext import commands
import json
import os
import sys
import discord
from discord.ext import commands
from classes import Cog_Extension
o_path = os.getcwd()
sys.path.append(o_path)
from stock_package import trendline as line
from stock_package import candle as candle
#from stock_package import xlstest

with open('setting.json','r', encoding='utf8') as jfile:
    jdata = json.load(jfile)

class stock_search(Cog_Extension):
    
    @commands.command()
    async def stock(self, ctx,stock_id,start,end = 0):
        print(stock_id)
        print(start)
        df_1 = line.stock_data(stock_id, start,end)
        print(df_1)
        line.line(df_1, stock_id)
        df_2 = candle.stock_data(stock_id, start,end)
        #print(df_2)
        candle.candle(df_2, stock_id)
        pic_1 = discord.File(jdata['stock_image'][0])
        pic_2 = discord.File(jdata['stock_image'][1])
        await ctx.send(file = pic_1)
        await ctx.send(file =pic_2)
        
def setup(bot):
    bot.add_cog(stock_search(bot))