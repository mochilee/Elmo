#導入 Discord.py
import discord
#client 是我們與 Discord 連結的橋樑，intents 是我們要求的權限

test = discord.Intents.default()
discord.message_content = True
client = discord.Client(intents=test)

#調用 event 函式庫
@client.event
#當機器人完成啟動時
async def on_ready():
    print('目前登入身份：', client.user)

@client.event
#當有訊息時
async def on_message(message):
    #排除自己的訊息，避免陷入無限循環
    if message.author == client.user:
        return
    #如果包含 ping，機器人回傳 pong
    if message.content == 'ping':
        print("test")
        await message.channel.send('pong')

class MyClient(discord.Client):
    async def on_message(self, message):
        if message.author == self.user:
            return

        if message.content.startswith('$hello'):
            await message.channel.send('Hello World!')

client.run('') #TOKEN 在剛剛 Discord Developer 那邊「BOT」頁面裡面