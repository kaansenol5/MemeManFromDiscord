import random,time
from discord.ext import commands
import praw
import requests
from bs4 import BeautifulSoup as bs
import json
used=[]
keyfile=open("login.json")
keys = json.load(keyfile)
cl_id = keys["reddit-key"]
cl_secret = keys["reddit-secret"]
r = reddit = praw.Reddit(
     client_id=cl_id,
     client_secret=cl_secret,
     user_agent="mememanfromdiscord"
 )

helpmsg = """
?meme for a meme
?copypasta for copypasta
?tifu for a tifu story
?help to display this message
?request:[feature] to request a feature (you will be banned from this right if you misuse)
If you want this feature to be free, dont misuse it!
?unsee to unsee the last thing you saw
?cringe for an ultracringe image that makes you want to [?unsee]
?code to view the github repo
"""



client=commands.Bot(command_prefix="?")

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
    if message.content.startswith(command):
        await message.channel.send(text)


async def ball(message):
    if message.content.startswith("?8ball"):
        choices=["yep","nope","maybe","idfc","no, definitely not, how can you be stupid enough to ask this","i dunno man maybe she does but idk","yes but idk","obviously maybe","i hate u","only if ur mom abortnites u","that will never happen, go cry in a dumpster","ur sick","go home","unknown","god says no but ur choice","ur as smart as a 5 month old coffe mug sitting near @MonsterSphaget#5549's pc, that will not happen"]
        choice=random.choice(choices)
        await message.channel.send(choice)


async def peepeesize(message):
    if message.content.startswith("?peepeesize"):
        user=message.content.replace("?peepeesize ","")
        size=random.randint(0,100)
        xmeters=random.choice(["Kilometets","Meters","Centimeters","Milimeters"])
        await message.channel.send(f"PeePee size of {user} is {size} {xmeters}")

async def epicrate(message):
    if message.content.startswith("?epicrate"):
        user=message.content.replace("?epicrate ","")
        rate=random.randint(0,100000)
        if user == r"*kaan*":
            rate=1000000000000000000000000000
        await message.channel.send(f"Epicrate of {user} is {rate} ")


async def hack(message):
    if message.content.startswith("?hack"):
        target=message.content.replace("?hack")
        await message.channel.send(f"Hacking {target}")
        await message.channel.send("IP address is 127.0.0.1")
        await message.channel.send(f"Abortnited {target}")




async def urbansearch(message):
    if message.content.startswith("?urban "):
        query=message.content.replace("?urban ","")
        print(query)
        r= requests.get(f"https://www.urbandictionary.com/define.php?term={query}")
        if r.status_code != 200:
            print(r.status_code)
            if r.status_code == 404:
                message.channel.send("That does not exist")

            return
        soup = bs(r.content,"html.parser")
        definition=soup.find("div","meaning").text
        await message.channel.send(definition)




async def main(message):
    await epicrate(message)
    await peepeesize(message)
    await ball(message)
    await sendReddit("?meme",random.choice(["dankmemes","memes","me_irl","historymemes"]),"img",message)
    await sendReddit("?unfunny",random.choice(["comedycemetery","terriblefacebookmemes"]),"img",message)
    await sendReddit("?türko", random.choice(["turkeyjerky", "shitposttc", "tamamahbapengelli", "kgbtr"]), "img", message)
    await sendReddit("?shitpost", "shitposting", "img", message)
    await sendMsg2("is kaan hawli", "kaan is hawli", message)
    await sendReddit("?copypasta","copypasta","txt",message)
    await sendReddit("?tifu","tifu","txt",message)
    await sendReddit("?unsee","eyebleach","img",message)
    await sendReddit("?cringe","cringetopia","img",message)
    await sendReddit("?showertoughts","showerthoughts","txt",message)
    await sendMsg("?githubrepo","https://github.com/kaansenol5/MemeManFromDiscord",message)
    await sendMsg2("hack","oh nononononono pls no hack my computor my mom bought thgis yesterday she will be so mad pls just take my ip 127.0.0.1 pls no hack me",message)
    await sendMsg("?help",helpmsg,message)
    await sendMsg("abeh","ABEH MOMENTS \n"*10,message)
    await sendReddit("?cursed","cursedimages","img",message)
    await urbansearch(message)
