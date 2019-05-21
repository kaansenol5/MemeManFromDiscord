from login import r, token  # login file, secret stuff
import random,time
from chatterbot  import ChatBot
from chatterbot.trainers import ListTrainer,UbuntuCorpusTrainer

used=[]

bot = ChatBot(
    'ChatBot-MemeMan',
    storage_adapter='chatterbot.storage.SQLStorageAdapter',
    logic_adapters=[
        {
            'import_path': 'chatterbot.logic.BestMatch'
        },
        {
            'import_path': 'chatterbot.logic.MathematicalEvaluation'
        },
        {
            'import_path':'chatterbot.logic.TimeLogicAdapter'
        }
    ]
)

 
#conversation = open('chatbot/converstions.txt','r').readlines()
 
trainer = UbuntuCorpusTrainer(bot)

trainer.train()

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
        if user == "MonsterSphaget":
            rate=1000000000000000000000000000
        await message.channel.send(f"Epicrate of {user} is {rate} ")


async def hack(message):
    if message.content.startswith("?hack"):
        target=message.content.replace("?hack")
        await message.channel.send(f"Hacking {target}")
        await message.channel.send("IP address is 127.0.0.1")
        await message.channel.send(f"Abortnited {target}")


async def talktochatbot(message):
    if message.content.startswith("?chatbot:"):
        dialogue=message.content.replace("?chatbot:","")
        botanswer=ChatBot.get_response(dialogue)
        message.channel.send(f"ChatBot: {botanswer}")
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
    await sendMsg("?help",helpmsg,message)
    await sendMsg("abeh","ABEH MOMENTS \n"*10,message)
    await sendMsg("?who is şenoli","he is my lord and he molested me",message)
    await sendMsg2("?hat",random.choice(["https://www.tilley.com/media/catalog/product/l/t/ltm6_khaki_a_1.jpg","http://www.wildearth.com.au/assets/full/793.jpg"]),message)