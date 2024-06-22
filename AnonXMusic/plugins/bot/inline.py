from pyrogram.types import (
    InlineKeyboardButton,
    InlineKeyboardMarkup,
    InlineQueryResultPhoto,
)
from youtubesearchpython.__future__ import VideosSearch

from AnonXMusic import app
from AnonXMusic.utils.inlinequery import answer
from config import BANNED_USERS


@app.on_inline_query(~BANNED_USERS)
async def inline_query_handler(client, query):
    text = query.query.strip().lower()
    answers = []
    if text.strip() == "":
        try:
            await client.answer_inline_query(query.id, results=answer, cache_time=10)
        except:
            return
    else:
        a = VideosSearch(text, limit=20)
        result = (await a.next()).get("result")
        for x in range(15):
            title = (result[x]["title"]).title()
            duration = result[x]["duration"]
            views = result[x]["viewCount"]["short"]
            thumbnail = result[x]["thumbnails"][0]["url"].split("?")[0]
            channellink = result[x]["channel"]["link"]
            channel = result[x]["channel"]["name"]
            link = result[x]["link"]
            published = result[x]["publishedTime"]
            description = f"{views} | {duration} ᴍɪɴᴜᴛᴇs | {channel}  | {published}"
            buttons = InlineKeyboardMarkup(
                [
                    [
                        InlineKeyboardButton(
                            text="ʏᴏᴜᴛᴜʙᴇ 🎄",
                            url=link,
                        )
                    ],
                ]
            )
            searched_text = f"""
❄ <b>𝙱𝙰𝚂̧𝙻𝙸𝙺 :</b> <a href={link}>{title}</a>

⏳ <b>𝚂𝚄̈𝚁𝙴  :</b> {duration} ᴍɪɴᴜᴛᴇs
👀 <b>𝙶𝙾̈𝚁𝚂𝙴𝙻 :</b> <code>{views}</code>
🎥 <b>𝙺𝙰𝙽𝙰𝙻 :</b> <a href={channellink}>{channel}</a>
⏰ <b>𝚈𝙰𝚈𝙸𝙽𝙻𝙰𝙽𝙳𝙸 :</b> {published}


<u><b>➻ 𝚂𝚊𝚝ı𝚛 𝙸̇𝚌̧𝚒 𝙰𝚛𝚊𝚖𝚊𝚢ı 𝙴𝚝𝚔𝚒𝚗𝚕𝚎𝚜̧𝚝𝚒𝚛𝚎𝚗 𝙺𝚒𝚜̧𝚒 {app.name}</b></u>"""
            answers.append(
                InlineQueryResultPhoto(
                    photo_url=thumbnail,
                    title=title,
                    thumb_url=thumbnail,
                    description=description,
                    caption=searched_text,
                    reply_markup=buttons,
                )
            )
        try:
            return await client.answer_inline_query(query.id, results=answers)
        except:
            return
