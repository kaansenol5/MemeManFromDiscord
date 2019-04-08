import discord
import pickle
from login import r, token
client=discord.Client()
used=[]
def save():
    with open("used","ab") as f:
        pickle.dump(used,f)
def load():
    with open("used","rb") as f:
        used=pickle.load(f)
load()

def sub(x):
    return r.subreddit(x)

def get_post_reddit(subreddit, type):
    for submission in subreddit.hot():
        if submission.url not in used and not submission.stickied:
            used.append(submission.url)
            if type == "img":
                return submission.url
            if type == "txt":
                return submission.title + "\n\n\n" + submission.selftext

@client.event
async def on_message(message):
    if message.content == "?meme":
        msg=get_post_reddit(sub("me_irl"),"img")
        print("sending meme")
        await client.send_message(message.channel,msg)
    if message.content == "?wallpaper":
        msg=get_post_reddit(sub("wallpapers"),"img")
        print("sending wallpaper")
        await client.send_message(message.channel,msg)
    if message.content == "?copypasta":
        print("sending copypasta")
        msg = get_post_reddit(sub("copypasta"),"txt")
        await client.send_message(message.channel, msg)
    if message.content == "?tifu":
        print("sending tifu")
        msg = get_post_reddit(sub("tifu"),"txt")
        await client.send_message(message.channel, msg)
client.run(token)