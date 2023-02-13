import discord
from discord.ext import commands
from classes import Cog_Extension
import json
import random

with open('setting.json','r', encoding='utf8') as jfile:
    jdata = json.load(jfile)

class react(Cog_Extension):
    
    @commands.command()
    async def image(self, ctx):
        random_pic = random.choice(jdata['pic'])
        pic = discord.File(random_pic)
        await ctx.send(file = pic)
        
    @commands.command()  
    async def web(self, ctx):
        random_pic = random.choice(jdata['url_pic'])
        await ctx.send(random_pic)
        
def setup(bot):
    bot.add_cog(react(bot))        