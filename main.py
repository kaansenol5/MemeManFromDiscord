import discord
import botstuff # just bot things
import login



@botstuff.client.event
async def on_ready():
    print("bot ready")



@botstuff.client.event
async def on_message(message):
    if message.content=="?shutdown" and message.author =="MonsterSphaget#5549":
        exit()
    await botstuff.main(message)
botstuff.client.run(login.token)
