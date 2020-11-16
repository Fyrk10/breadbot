import discord
from discord.ext import commands
from discord.voice_client import VoiceClient
import requests
from Scraping import Heads
import os

Client = commands.Bot(command_prefix= "!")

def users(ctx):
    return ctx.author.id == 385910511436431360

@Client.event
async def on_ready():
    activity = discord.Game(name="on BreadMC.com", type=4)
    await Client.change_presence(status=discord.Status.online, activity=activity)
    print("Bot is READY")
    

@Client.command()
async def server(ctx):
    embed = discord.Embed(
        title = "Server Status",
        description = "See what is happening on the server! To see and chat with players in real time, click [**here**](http://map.breadmc.com/ 'map.breadmc.com').",
        colour=discord.Colour.orange(),
    )
    embed.set_image(url="https://cdn.discordapp.com/attachments/732656102591955006/774042763440291860/ImageDynmap.PNG")
    playerzzz = ""
    if len(Heads()) > 0: 
        #embed.add_field(name="ㅤ", value="ㅤ", inline="False")
        for player in Heads():
            playerzzz += player + " "

        embed.add_field(name="Online Players: " + str(len(Heads())), value=playerzzz, inline="False")
        embed.set_footer(text="I don't know what to put here anymore DZ36 is kinda admin.")
    else:
        embed.add_field(name="Online Players: 0" , value="Nobody is here...", inline="False")


    await ctx.send(embed=embed)

@Client.command()
async def ip(ctx):
    embed = discord.Embed(
    title = "BreadMC Server IP address",
    description = "IP address: **breadmc.com**",
    colour=discord.Colour.orange(),
    )

    await ctx.send(embed=embed )


@Client.command()
async def poll(ctx, *message):
    deletedmesssage = await ctx.channel.fetch_message(int(ctx.channel.last_message_id))
    author = str(deletedmesssage.author)
    await deletedmesssage.delete()
    embed = discord.Embed(
        title = str(message).replace(",","").replace("(", "").replace(")", "").replace("'", "")    ,
        description = "React with an emote to vote!",
        colouFr = discord.Colour.orange(),
    )
    await ctx.send("@everyone")
    embed.set_footer(text=" Poll created by: " + author)
    await ctx.send(embed=embed)
    emojis =["👍", "👎"]
    message = await ctx.channel.fetch_message(int(ctx.channel.last_message_id))
    for emoji in emojis:
        await message.add_reaction(emoji=emoji)

Client.run("TOKEN")