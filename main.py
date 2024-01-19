import json
from pyrogram import *
from pyrogram.types import *
from pyromod import listen
# =======================================
with open("config.json", "r") as confing_file:
    confing_data = json.load(confing_file)
api_id = confing_data["api_id"]
api_hash = confing_data["api_hash"]
bot_token = confing_data["bot_token"]
# =======================================
app = Client("FullToolsBot",api_id=api_id,api_hash=api_hash,bot_token=bot_token)
# =======================================
#! Database
# =======================================
Keyboard = ReplyKeyboardMarkup(
    [
      ["🃏 FlashCard 🃏","💆‍♂️ BMI 💆‍♂️"],
      ["👨‍💻 Developer 👨‍💻"]  
    ],
)
# =======================================

@app.on_message(filters.command("start"))
async def Start(client, message):
    await message.reply_text(f"""🔥Hello <b>{message.from_user.mention}</b> ,
🧰 A toolbox that comes in handy everywhere""",
                             reply_markup=Keyboard, parse_mode=enums.ParseMode.HTML)
# =====================================================================
async def Home(client, message):
        await message.reply_text(f"""What can I do?
Use the options below👇""",reply_markup=Keyboard)
# =====================================================================
# =======================================
@app.on_message(filters.regex("^👨‍💻 Developer 👨‍💻$"))
async def Developer(client, message):
    await message.reply_text("Communication with programming", reply_markup=InlineKeyboardMarkup(
        [
            [
                InlineKeyboardButton(
                    "Telegram",
                    url="https://t.me/MrTakDev"
                ),
                InlineKeyboardButton(
                    "Twitter",
                    url="https://twitter.com/erfan_banaei"
                ),
            ],
            [ 
                InlineKeyboardButton(
                    "Linkedin",
                    url="https://www.linkedin.com/in/erfanbanaeii"
                ),
                InlineKeyboardButton(
                    "Github",
                    url="https://github.com/erfanbanaei/"
                )
        ]
        ]
    )
    )
# =======================================
app.run()