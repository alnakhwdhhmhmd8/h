import pyrogram, sys
from pyrogram import Client, filters, enums
from config import *
import asyncio
from pyrogram.types import (InlineQueryResultArticle, InputTextMessageContent, InlineKeyboardMarkup, InlineKeyboardButton)

pyro = pyrogram.__version__
py = sys.version

@app.on_message(filters.command(["سورس","السورس"], prefixes=f".") & filters.me)
async def ping(app, msg):
  await msg.delete()
  txt = f"""
• 𝗛𝗲𝗹𝗹𝗼 𝗗𝗲𝗮𝗿 : {msg.from_user.mention}
— — — — — — — — —
• 𝗗𝗲𝘃 𝗦𝗼𝘂𝗿𝗰𝗲 : @wwvvwl
• 𝗖𝗵𝗮𝗻𝗻𝗲𝗹 𝗦𝗼𝘂𝗿𝗰𝗲 : @xvwwvl
• [𝗣𝘆𝗿𝗼𝗴𝗿𝗮𝗺 {pyro}](https://docs.pyrogram.org/)
• 𝗣𝘆𝘁𝗵𝗼𝗻 {py}
  """
  await app.send_video(msg.chat.id,
  video="https://t.me/ydoydkgddyo/76",
  caption=txt, reply_markup=InlineKeyboardMarkup([[InlineKeyboardButton(text="𝐋𝐄𝐀𝐃𝐄𝐑 𝐒𝐀𝐃𝐃𝐀𝐌 𝐇𝐔𝐒𝐒𝐄𝐈𝐍", url=f"https://t.me/wwvvwl")]]))