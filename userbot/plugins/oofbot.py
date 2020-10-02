"""Commands:
.oofbot"""

import asyncio
import logging
logging.basicConfig(format='[%(levelname) 5s/%(asctime)s] %(name)s: %(message)s',
                    level=logging.WARNING)
import datetime
from collections import deque
from telethon import events
from telethon.errors.rpcerrorlist import YouBlockedUserError
from telethon.tl.functions.account import UpdateNotifySettingsRequest
import asyncio
from userbot import CMD_HELP, ALIVE_NAME, bot
from userbot.system import dev_cmd


# ================= CONSTANT =================
DEFAULTUSER = str(ALIVE_NAME) if ALIVE_NAME else "UserBot"
# ============================================


@bot.on(dev_cmd(pattern="oofbot", outgoing=True))
async def _(event):
    if event.fwd_from:
        return
    animation_interval = 1.0
    animation_ttl = range(0, 100)
    #input_str = event.pattern_match.group(1)
    #if input_str == "oofbot":
    await event.edit("oofbot")
    animation_chars = [

            "⚠️O",

            "⚠️OO",

            "⚠️OOF",

            "⚠️OOF-",

            "⚠️OOF-b",

            "⚠️OOF-bo",

            "⚠️OOF-bot⚙️"

            "da parte di @MarvynSTAR e @doggy_cheems👍🏻"


        ]

    for i in animation_ttl:        
            await asyncio.sleep(animation_interval)        
            await event.edit(animation_chars[i % 8])

