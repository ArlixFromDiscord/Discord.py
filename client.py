#Anything not working? Report it to the Issues tab and I will help you
import discord
from discord.ext.commands import Bot
from discord.ext import commands

client = discord.Client()
bot_prefix= "!"
Client = commands.Bot(command_prefix=bot_prefix)

@client.event
async def on_ready():
    await client.change_presence(game=discord.Game(name='with Arlix in his SLEEP'))
    print ("hi dad")

@client.event
async def on_message(message):
    if message.content == "!help":
        em = discord.Embed(title='ALX-Bot v0.1', description='These are the commands **you** can use with ALX-Bot.', colour=0x00ff00)
        em.add_field(name="!help", value="Shows this message.")
        await client.send_message(message.author, embed=em)
    if message.content == "!help":
        em = discord.Embed(title=':mailbox_with_mail: Check DMs', color=0x00ff00)
        await client.send_message(message.channel, embed=em)
 
client.run("MjM5NDgxMTMyNzA4NjU5MjAw.DYzQmg.iBQAEtXrQfljfTx1ui37r12egHI")
