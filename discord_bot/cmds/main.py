import discord
from discord.ext import commands
from classes import Cog_Extension

class Main(Cog_Extension):
 
    
    @commands.command()
    async def ping(self, ctx):
        await ctx.send(F'{round(self.bot.latency*1000)}(ms)')
        
    @commands.command()     
    async def test(self, ctx):
        await ctx.send('test message')
        
        
    @commands.command()     
    async def clean(self, ctx, num = 10):
        await ctx.channel.purge(limit = num + 1)
        
    @commands.command()     
    async def sayd(self, ctx, *,msg):
        await ctx.message.delete()
        await ctx.send(msg)    
def setup(bot):
    bot.add_cog(Main(bot))
    