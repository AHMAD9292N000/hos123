from pyrogram.types import InlineKeyboardButton

import config
from MatrixMusic import app

def start_panel(_):
    buttons = [
        [
            InlineKeyboardButton(
                text="اضغط لاضافتي لمجموعتك✅", url=f"https://t.me/{app.username}?startgroup=true"
            ),
            InlineKeyboardButton(text="𝙶𝚁𝙾̀𝚄𝙿", url= "https://t.me/CZCRR0"),
        ],
    ]
    return buttons


def private_panel(_):
    buttons = [
        [
            InlineKeyboardButton(
                text="اضغط لاضافتي لمجموعتك✅",
                url=f"https://t.me/{app.username}?startgroup=true",
            )
        ],
        
        [
            InlineKeyboardButton(text="مطور البوت", user_id=config.OWNER_ID),
            InlineKeyboardButton(text="𝙶𝚁𝙾̀𝚄𝙿", url=f"https://t.me/CZCRR0"), 
        ],
        [
            
            InlineKeyboardButton(text="𝑺𝑶𝑼𝑹𝑪𝑬 Y Z N ", url=f"https://t.me/F_U_01") , 
        ],
    ]
    return buttons
