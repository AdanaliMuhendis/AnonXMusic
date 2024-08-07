import asyncio
from datetime import datetime

from pyrogram.enums import ChatType

import config
from AnonXMusic import app
from AnonXMusic.core.call import Anony, autoend
from AnonXMusic.utils.database import get_client, is_active_chat, is_autoend


async def auto_leave():
    if config.AUTO_LEAVING_ASSISTANT:
        while not await asyncio.sleep(900):
            from AnonXMusic.core.userbot import assistants

            for num in assistants:
                client = await get_client(num)
                left = 0
                try:
                    async for i in client.get_dialogs():
                        if i.chat.type in [
                            ChatType.SUPERGROUP,
                            ChatType.GROUP,
                            ChatType.CHANNEL,
                        ]:
                            if (
                                i.chat.id != config.LOGGER_ID
                                and i.chat.id != -1001891680771
                                and i.chat.id != -1001923310875
                            ):
                                if left == 20:
                                    continue
                                if not await is_active_chat(i.chat.id):
                                    try:
                                        await client.leave_chat(i.chat.id)
                                        left += 5
                                    except:
                                        continue
                except:
                    pass


asyncio.create_task(auto_leave())


async def auto_end():
    while not await asyncio.sleep(5):
        ender = await is_autoend()
        if not ender:
            continue
        for chat_id in autoend:
            timer = autoend.get(chat_id)
            if not timer:
                continue
            if datetime.now() > timer:
                if not await is_active_chat(chat_id):
                    autoend[chat_id] = {}
                    continue
                autoend[chat_id] = {}
                try:
                    await Anony.stop_stream(chat_id)
                except:
                    continue
                try:
                    await app.send_message(
                        chat_id,
                        "<b>» 𝚂𝚎𝚜𝚕𝚒 𝚂𝚘𝚑𝚋𝚎𝚝𝚝𝚎 𝙱𝚎𝚗𝚒 𝚈𝚊𝚕𝚗ı𝚣 𝙱ı𝚛𝚊𝚔𝚝ı𝚐̆ı𝚗ı𝚣 𝙸̇𝚌̧𝚒𝚗 𝙶𝚒𝚍𝚒𝚢𝚘𝚛𝚞𝚖🥹🥹🥹🥲 <b>",
                    )
                except:
                    continue


asyncio.create_task(auto_end())
