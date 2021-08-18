
#WICHTIG FÜRS WEITER MACHEN  message.channel.send durch das erstezten  message.author.send.....
import time

import discord
import secrets
import string
import asyncio
from discord.ext.commands import Bot
from discord.ext import commands


TOKEN = "ODc3Njc3MjYyMzU3NTQwOTY1.YR2GpQ.hTGkZKstlPzeO7K1LbS5wHrvNEA"
chars = string.digits + string.ascii_letters +string.punctuation
chars2 = string.ascii_lowercase + string.ascii_uppercase




client = commands.Bot(command_prefix="$")


@client.event
async def on_ready():
    print("Erfolg wurde als {0.user} eingeloggt ! ".format(client))

#Hier PassGenertoren PassGen(Zahl) ist die normale varriante und PassChr(Zahl) sind nur Buchstaben
@client.event
async def on_message(message):
    if message.author == client.user:
        return
    if message.content.startswith("$PassGen10"):
        await message.author.send("".join(secrets.choice(chars)for _ in range (10)))
        await message.delete()
        return
    if message.content.startswith("$PassGen20"):
        await message.author.send("".join(secrets.choice(chars)for _ in range (20)))
        await message.delete()
        return
    if message.content.startswith("$PassGen5"):
        await message.author.send("".join(secrets.choice(chars)for _ in range (5)))
        await message.delete()
        return
    if message.content.startswith("$PassGen15"):
        await message.author.send("".join(secrets.choice(chars)for _ in range (15)))
        await message.delete()
        return
    if message.content.startswith("$PassChr10"):
        await message.author.send("".join(secrets.choice(chars2)for _ in range (10)))
        await message.delete()
        return
    if message.content.startswith("$PassChr20"):
        await message.author.send("".join(secrets.choice(chars2)for _ in range (20)))
        await message.delete()
        return
    if message.content.startswith("$PassChr5"):
        await message.author.send("".join(secrets.choice(chars2)for _ in range (5)))
        await message.delete()
        return
    if message.content.startswith("$PassChr15"):
        await message.author.send("".join(secrets.choice(chars2)for _ in range (15)))
        await message.delete()
        return
    if message.content.startswith("$PassHelp"):
        await message.channel.send("Use $PassGen5/10/15/20 or $PassChr5/10/15/20 PassChr ist without numbers and charakters.",delete_after=500)
        time.sleep(500)
        await message.delete()
        return










client.run(TOKEN)






