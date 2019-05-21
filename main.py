import discord
import botstuff # just bot things
import login



client=discord.Client()



@client.event
async def on_ready():
    print("dametucosita")



@client.event
async def on_message(message):
    if message.content=="?shutdown" and message.author =="MonsterSphaget#5549":
        exit()
    await botstuff.main(message)
client.run(login.token)
