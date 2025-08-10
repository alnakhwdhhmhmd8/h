from pyrogram import Client, idle
from pyromod import listen



bot = Client(
    "FR3ON",
    api_id=28929515,
    api_hash="6cc248d1b0d626232ef66ac5153370b8",
    bot_token="7936597041:AAGQAHtCckYIMvWwY8NPZN8fv5yws2Q50Xw",
    plugins=dict(root="FR3ON")
    )

DEVS = ["wwvvwl", "wwvvwl"] 

bot_id = bot.bot_token.split(":")[0]

async def start_ahmedbot():
    print("تم تشغيل الصانع بنجاح..🕊")
    await bot.start()
    for hh in DEVS:
        try:
            await bot.send_message(hh, "**تم تشغيل الصانع بنجاح ...! ⚡**")
        except:
            pass
    await idle()
