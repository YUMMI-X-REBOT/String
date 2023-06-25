from pyrogram import Client, filters
from pyrogram.types import InlineKeyboardMarkup, InlineKeyboardButton, Message

from config import OWNER_ID


def filter(cmd: str):
    return filters.private & filters.incoming & filters.command(cmd)

@Client.on_message(filter("start"))
async def start(bot: Client, msg: Message):
    me2 = (await bot.get_me()).mention
    await bot.send_message(
        chat_id=msg.chat.id,
        text=f"""Hᴇʏ {msg.from_user.mention},

Tʜɪs ɪs sᴛʀɪɴɢ sᴇssɪᴏɴ,
Aɴ ᴏᴘᴇɴ sᴏᴜʀᴄᴇ sᴛʀɪɴɢ sᴇssɪᴏɴ ɢᴇɴᴇʀᴀᴛᴏʀ ʙᴏᴛ, ᴡʀɪᴛᴛᴇɴ ɪɴ ᴩʏᴛʜᴏɴ ᴡɪᴛʜ ᴛʜᴇ ʜᴇʟᴩ ᴏғ ᴩʏʀᴏɢʀᴀᴍ.

Mᴀᴅᴇ ᴡɪᴛʜ 🍁 ʙʏ : [Tʀɪᴄᴋʏ✦Rᴀᴊ](tg://user?id={OWNER_ID}) !""",
        reply_markup=InlineKeyboardMarkup(
            [
                [
                    InlineKeyboardButton(text="🍁 Gᴇɴᴇʀᴀᴛᴇ Sᴇssɪᴏɴ🥀", callback_data="generate")
                ],
                [
                    InlineKeyboardButton("☆Gʀᴏᴜᴘ☆", url="https://t.me/YummiSupport"),
                    InlineKeyboardButton("☆Cʜsɴɴᴇʟ☆", url="https://t.me/YummiUpdate")
                ],
                [
                    InlineKeyboardButton("☆Oᴡɴᴇᴛ✦xD☆", user_id=OWNER_ID)
                ]
            ]
        ),
        disable_web_page_preview=True,
    )
