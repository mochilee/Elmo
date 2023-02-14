import discord
from discord.ext import commands
from classes import Cog_Extension
import json

with open('setting.json','r', encoding='utf8') as jfile:
    jdata = json.load(jfile)
    
class event(Cog_Extension):
 
    
    @commands.Cog.listener()
    async def on_message(self, msg):
        
        for i in range(len(msg.content) - 2):
            if msg.content[i].lower() == ("l") and msg.content[(i + 1)].lower() == ("o") and msg.content[(i + 2)].lower() == ("l") and msg.author != self.bot.user:
                await msg.channel.send('打三小lol')
                break
         
        for i in range(len(msg.content)):        
            if msg.content[i] == '打' and msg.author != self.bot.user:    
                await msg.channel.send('打手槍拉打')
                break
        
        if msg.content == '1234' and msg.author != self.bot.user:
            await msg.channel.send('5678')
        
        
        
def setup(bot):
    bot.add_cog(event(bot))
    