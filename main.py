import discord

from login import r, token  # login file, secret stuff

client=discord.Client()
used=[]
helpmsg = """
?meme for a meme
?copypasta for copypasta
?tifu for a tifu story
?help to display this message
?img/r/* for an image/gif from a subreddit
?txt/r/* for a text from a subreddit"""

def sub(x):
    return r.subreddit(x)


def get_post_reddit(subr, type):
    global used
    print("peepee")
    subreddit = sub(subr)
    for submission in subreddit.hot():
        if not submission.stickied and not submission.over_18:
            if type == "img":
                return submission.url
            if type == "txt":
                return submission.title + "\n\n\n" + submission.selftext


async def sendMsg(command, text, message):
    if message.content == command:
        message.channel.send(text)


async def sendReddit(command, subreddit, type, message):
    if message.content == command:
        msg = get_post_reddit(subreddit, type)
        if not f"{message.server}:{msg}" in used:
            used.append(f"{message.server}:{msg}")
            message.channel.send(msg)


async def sendMsg2(command, text, message):
    if command in message.content:
        message.channel.send(text)
@client.event
async def on_message(message):
    await sendReddit("?unsee", "eyebleach", "img", message)
    await sendReddit("?meme", "me_irl", "img", message)
    await sendReddit("?copypasta", "copypasta", "txt", message)
    await sendReddit("?tifu", "tifu", "txt", message)
    await sendMsg2("hack",
                   "Pleas no hack my pc my ip is 127.0.0.1 my mom just buyed this computer have mercy", message)
    await sendReddit("?cringe", "cringetopia", "img", message)
    await sendMsg("?code", "https://www.github.com/kaansenol5/mememandiscord", message)
client.run(token)
