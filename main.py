import discord
from login import r, token  # login file, secret stuff



client=discord.Client()
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


used=[]
bannedusers=open("bannedusers.txt","r").read()
#banlist=list(open("banlist","r").read())
def sub(x):
    return r.subreddit(x)

#def banuser(user):   //TODO: fix this shit
    #with open("bannedusers.txt","a") as f:
        #f.write(str(user)+"\n")
    

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

async def feature_request(message):

    if "?request" in message.content:
        print("tried request")
        if str(message.author) not in bannedusers:
            
            #for word in banlist:
                #if word in message.content:
                 #   #banuser(message.author) TODO fix this shit
                  #  break
                
            with open("requests.txt", "a") as f:
                f.write(f"{message.author} on {message.guild} requests {message.content.replace('?request:','')} \n\n")
                print("request made")
                #break
        else:
            print("retard")


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
    await feature_request(message)
print("there u go")
client.run(token)
