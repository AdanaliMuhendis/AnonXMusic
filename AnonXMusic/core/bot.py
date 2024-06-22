from pyrogram import Client, errors
from pyrogram.enums import ChatMemberStatus, ParseMode

import config

from ..logging import LOGGER


class Anony(Client):
    def __init__(self):
        LOGGER(__name__).info(f"𝙰𝙻𝙴𝙼 𝙼𝚄̈𝚉𝙸̇𝙺 𝙱𝙰𝚂̧𝙻𝙸𝚈𝙾𝚁...")
        super().__init__(
            name="AnonXMusic",
            api_id=config.API_ID,
            api_hash=config.API_HASH,
            bot_token=config.BOT_TOKEN,
            in_memory=True,
            parse_mode=ParseMode.HTML,
            max_concurrent_transmissions=7,
        )

    async def start(self):
        await super().start()
        self.id = self.me.id
        self.name = self.me.first_name + " " + (self.me.last_name or "")
        self.username = self.me.username
        self.mention = self.me.mention

        try:
            await self.send_message(
                chat_id=config.LOGGER_ID,
                text=f"<u><b>» {self.mention} 𝙰𝙻𝙴𝙼 𝙼𝚄̈𝚉𝙸̇𝙺 𝙱𝙰𝚂̧𝙻𝙰𝙳𝙸 :</b><u>\n\n𝙸𝙳 : <code>{self.id}</code>\n𝙰𝙳𝙸 : {self.name}\n𝙺𝚄𝙻𝙻𝙰𝙽𝙸𝙲𝙸 𝙰𝙳𝙸 : @{self.username}",
            )
        except (errors.ChannelInvalid, errors.PeerIdInvalid):
            LOGGER(__name__).error(
                "𝙻𝚞̈𝚝𝚏𝚎𝚗 𝙱𝚘𝚝𝚞 𝙻𝚘𝚐 𝙺𝚊𝚗𝚊𝚕ı𝚗𝚊 𝙴𝚔𝚕𝚎𝚢𝚒𝚗...."
            )
            exit()
        except Exception as ex:
            LOGGER(__name__).error(
                f"𝙱𝚘𝚝 𝙷𝚊𝚝𝚊 𝚅𝚎𝚛𝚍𝚒...\n  𝚂𝚎𝚋𝚎𝚋𝚒 : {type(ex).__name__}."
            )
            exit()

        a = await self.get_chat_member(config.LOGGER_ID, self.id)
        if a.status != ChatMemberStatus.ADMINISTRATOR:
            LOGGER(__name__).error(
                "𝙻𝚞̈𝚝𝚏𝚎𝚗 𝙱𝚘𝚝𝚞𝚗 𝙲̧𝚊𝚕ı𝚜̧𝚖𝚊𝚜ı 𝙸̇𝚌̧𝚒𝚗 𝚈𝚎𝚝𝚔𝚒 𝚅𝚎𝚛𝚒𝚗..."
            )
            exit()
        LOGGER(__name__).info(f"Music Bot Started as {self.name}")

    async def stop(self):
        await super().stop()
