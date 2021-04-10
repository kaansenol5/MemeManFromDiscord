import discord
import botstuff # just bot things
import json


"""
SHITTI CODE SHITTI CODE
"""
tokenfile = open("login.json")

json = json.load(tokenfile)
token = json["discord-token"]

@botstuff.client.event
async def on_ready():
    print("bot ready")



@botstuff.client.event
async def on_message(message):
    await botstuff.main(message)
botstuff.client.run(token)
