"""Restart or Terminate the bot from any chat
Commands:
.restart
.shutdown"""
import asyncio
import os
import sys

from telethon import events
from userbot import bot, ALIVE_NAME
from userbot.system import dev_cmd

# ================= CONSTANT =================
DEFAULTUSER = str(ALIVE_NAME) if ALIVE_NAME else "100101110"
# ============================================


@bot.on(dev_cmd("restart"))
async def _(event):
    if event.fwd_from:
        return
    await event.edit(f"`{DEFAULTUSER}:`**Riavvio in corso...**\n**mi sto riavviando se non mi accendo controlla il log heroku vedi se sono online con `.test`**")
    await bot.disconnect()
    # https://archive.is/im3rt
    os.execl(sys.executable, sys.executable, *sys.argv)
    # You probably don't need it but whatever
    quit()


@bot.on(dev_cmd("shutdown"))
async def _(event):
    if event.fwd_from:
        return
    await event.edit(f"`{DEFAULTUSER}:`**Userbot spento**\n**puoi avviarmi manualmente da heroku**")
    await bot.disconnect()
