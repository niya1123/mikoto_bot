import discord
import discord_token
import asyncio
import serifu
import re
import random
from datetime import datetime

client = discord.Client()  # botの起動に必要。

channel = client.get_channel(discord_token.token_id)  # channelの取得


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

    # if client.user in client.users:
    #     """
    #     話しかけられたら返事をするのテンプレ。
    #     """
    #     if client.user != message.author:
    #         print(message.content)
    #         reply = f'{message.author.mention}呼んだ？'
    #         await message.channel.send(reply)

    if message.content.startswith("<@!"):

        if client.user != message.author:

            if message.content.find("ビリビリ") != -1:
                reply = select_normal_serifu(
                    message.author.mention, serifu.normal_serifu["ビリビリ"])

            elif message.content.find("おはよう") != -1:
                reply = select_normal_serifu(
                    message.author.mention, serifu.normal_serifu["おはよう"])

            elif message.content.find("今何時") != -1:
                reply = time_reply(message.author.mention)

            elif message.content.find("デレて") != -1:
                tmp = serifu.normal_serifu["デレ"]
                random.shuffle(tmp)
                reply = select_normal_serifu(message.author.mention, tmp[0])

            else:
                reply = f'{message.author.mention} 何言ってるか分かんないわ'

            await message.channel.send(reply)


def select_normal_serifu(mention, res):
    """
    決まり切った質問に対してのリプライをするもの。

    parameters
    ----------
    mention: str
        メッセージを送ってきた相手のuser_id。

    key: str
        serifu.pyのnormal_serifuという辞書のkey。    
    """
    return f'{mention} {res}'


def time_reply(mention):
    """
    時間を聞かれた時のリプライをするもの。

    parameters
    ----------
    mention: str
        メッセージを送ってきた相手のuser_id。

    """
    return f'{mention} 今は、{datetime.now().strftime("%Y/%m/%d %H:%M:%S")}よ。'


client.run(discord_token.token_id)  # botの起動。
