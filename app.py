import discord, discord_token, asyncio



client = discord.Client() #botの起動に必要。

channel = client.get_channel(discord_token.token_id) #channelの取得

@client.event
async def on_ready():
    """
    ログイン時の通知。
    """
    print("ログインしました")

@client.event
async def on_message(message):
    """
    メッセージ受信時のイベントの処理を行うところ。

    parameters
    ----------
    message: discord.message.Message
        受信したメッセージ。
    """

    if message.content.startswith('!neko'):
        """
        !nekoというメッセージを受け取ったときにゃーんと返す。
        """
        reply = 'にゃーん'
        await message.channel.send(reply)

    if message.content.startswith('!bye'):
        """
        botがログアウトする。
        """
        await client.close()    

    if client.user in client.users:
        """
        話しかけられたら返事をするのテンプレ。
        """
        if client.user != message.author:
            reply = f'{message.author.mention}呼んだ？'
            await message.channel.send(reply)

client.run(discord_token.token_id)



        