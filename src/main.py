import discord

from login import r, token #login file, secret stuff

client=discord.Client()
used=[]
f = open("used", "wb")
helpmsg = """
?meme for a meme
?wallpaper for a wallpaper
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
        if submission.url not in used and not submission.stickied and not submission.over_18:
            used.append(submission.url)
            if type == "img":
                return submission.url
            if type == "txt":
                return submission.title + "\n\n\n" + submission.selftext


async def sendMsg(command, subreddit, message, type, reddit, text=None):
    if message.content == command:
        if reddit:
            msg = get_post_reddit(subreddit, type)
            print(command)
            await client.send_message(message.channel, msg)
        else:
            await client.send_message(message.channel, text)
@client.event
async def on_message(message):
    await sendMsg("?meme", "me_irl", message, "img", True)
    await sendMsg("?wallpaper", "wallpapers", message, "img", True)
    await sendMsg("?tifu", "tifu", message, "txt", True)
    await sendMsg("?copypasta", "copypasta", message, "txt", True)
    await sendMsg("?help", None, message, None, False, text=helpmsg)
    if "?txt/r/" in message.content:
        subreddit = message.content.replace("?txt/r/", "")
        await client.send_message(message.channel, get_post_reddit(subreddit, "txt"))
    if "img/r/" in message.content:
        subreddit = message.content.replace("?img/r/", "")
        await client.send_message(message.channel, get_post_reddit(subreddit, "img"))
    await sendMsg("i will hack ur pc", None, message, None, False,
                  text="Pleas no hack my pc my ip is 127.0.0.1 my mom just buyed this computer have mercy")
    await sendMsg("Özgür is a retard", None, message, None, False, text="Yes he is")
    await sendMsg("?cringe", "criingetopia", message, "img", True)
    await sendMsg("?code", None, message, None, False, text="")
client.run(token)
