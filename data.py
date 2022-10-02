from pyrogram.types import InlineKeyboardButton


class Data:
    generate_single_button = [InlineKeyboardButton("✨ ɢᴇɴᴇʀᴀᴛᴇ sᴇssɪᴏɴ ✨", callback_data="generate")]

    generate_button = [generate_single_button]

    buttons = [
        generate_single_button,
        [InlineKeyboardButton("⭙ sᴜᴩᴩᴏʀᴛ ⭙", url="https://t.me/Uputtsupport"),
         InlineKeyboardButton("⭙ ᴅᴇᴠᴇʟᴏᴩᴇʀ ⭙", url="https://t.me/Uputraa"),
        ],
    ]

    START = """
Hᴇʏ {},

Iᴍ {},
Di buat untuk Membantu Anda Mengambil String Session Telegram dengan Mudah dan AMAN!

Mᴀᴅᴇ ᴡɪᴛʜ 🖤 ʙʏ : [𝐔𝐩𝐮𝐭𝐭](https://t.me/Uputraa) !
    """
