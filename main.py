import discord
import botstuff # just bot things
import login


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


@client.event
async def on_ready():
    print("dametucosita")



@client.event
async def on_message(message):
    await botstuff.main(message)
print("there u go")
client.run(login.token)
