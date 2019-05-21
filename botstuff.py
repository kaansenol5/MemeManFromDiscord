from login import r, token  # login file, secret stuff
import random

used=[]
def sub(x):
    return r.subreddit(x)
    

def get_post_reddit(subr, type, message):
    global used
    print("peepee")
    subreddit = sub(subr)
    for submission in subreddit.hot():
        if not submission.stickied  and not f"{message.guild}:{submission.url}" in used and not submission.over_18:
            if type == "img":
                return submission.url
            if type == "txt":
                return submission.title + "\n\n\n" + submission.selftext


async def sendMsg(command, text, message):
    if message.content == command:
        await message.channel.send(text)


async def sendReddit(command, subreddit, type, message):
    if message.content == command:
        msg = get_post_reddit(subreddit, type, message)
        if not f"{message.guild}:{msg}" in used:
            used.append(f"{message.guild}:{msg}")
            await message.channel.send(msg)


async def sendMsg2(command, text, message):
    if command in message.content:
        await message.channel.send(text)


async def ball(message):
    if message.content.startswith("?8ball"):
        choices=["yep","nope","maybe","idfc","no, definitely not, how can you be stupid enough to ask this","i dunno man maybe she does but idk","yes but idk","obviously maybe"]
        choice=random.choice(choices)
        await message.channel.send(choice)


async def peepeesize(message):
    if message.content.startswith("?peepeesize"):
        user=message.content.replace("?peepeesize","")
        size=random.randint(0,100)
        if user == "MonsterSphaget":
            size=1000000000000000000000000000
            xmeters="Kilometers"
        else:
            xmeters=random.choice(["Centimeters","Kilometers","Milimeters"])
        await message.channel.send(f"PeePee size of {user} is {size} {xmeters}")

async def epicrate(message):
    if message.content.startswith("?epicrate"):
        user=message.content.replace("?epicrate","")
        rate=random.randint(0,100000)
        if user == "MonsterSphaget":
            rate=1000000000000000000000000000
        await message.channel.send(f"Epicrate of this person is {rate} ")





#TODO commit despasito


async def main(message):
    await epicrate(message)
    await peepeesize(message)
    await ball(message)
    await sendReddit("?meme",random.choice(["dankmemes","memes","me_irl","historymemes"]),"img",message)
    await sendReddit("?unfunny",random.choice(["comedycemetery","okbuddyretard","terriblefacebookmemes"]),"img",message)
    await sendReddit("?copypasta","copypasta","txt",message)
    await sendReddit("?tifu","tifu","txt",message)
    await sendReddit("?unsee","eyebleach","img",message)
    await sendReddit("?cringe","cringetopia","img",message)
    await sendReddit("?showertoughts","showerthoughts","txt",message)
    await sendMsg("?code","https://github.com/kaansenol5/MemeManFromDiscord",message)
    await sendMsg2("hack","oh nononononono pls no hack my computor my mom bought thgis yesterday she will be so mad pls just take my ip 127.0.0.1 pls no hack me",message)
    