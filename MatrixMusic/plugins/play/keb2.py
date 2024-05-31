import asyncio
import config
from pyrogram import Client, filters
from pyrogram import filters
from strings.filters import command
from MatrixMusic import app
from config import OWNER_ID
from MatrixMusic.misc import SUDOERS
from strings.filters import command
from pyrogram.types import InlineKeyboardButton, InlineKeyboardMarkup, Message, ReplyKeyboardMarkup
from pyrogram.types import (InlineKeyboardButton,CallbackQuery,InlineKeyboardMarkup, Message)
from MatrixMusic import (Apple, Resso, SoundCloud, Spotify, Telegram, YouTube, app)
from MatrixMusic.misc import SUDOERS
import sys
from os import getenv

OWNER_ID = getenv("OWNER_ID")
OWNER_USER_NAME = getenv("OWNER_USER_NAME")
NEON = getenv("NEON")

OWNER = getenv("OWNER")

from dotenv import load_dotenv
import re


@app.on_message(command(["كيب", "✭ رجوع"]) & SUDOERS)

async def crsourceowner(client: Client, message: Message):
    text = REPLY_MESSAGE
    reply_markup = ReplyKeyboardMarkup(REPLY_MESSAGE_BUTTONS, one_time_keyboard=True, resize_keyboard=True)
    await message.reply(
        text=text,
        reply_markup=reply_markup
    )


REPLY_MESSAGE = "**👋︙مـرحـبـا بـك عـزيـزي الـمـطـور ♥️**\n**✨︙فــي قـائـمـة التحـكـم بـالـبـوت💞**"

REPLY_MESSAGE_BUTTONS = [
    [
        ("✭ W𝒆𝒍𝒐𝒎𝒆 𝒕𝒐 𝒔𝒐𝒖𝒓𝒄𝒆 Y Z N 𝒎𝒖𝒔𝒊𝒄 ✭"),
    ],
    [
        ("✭ قسم الاذاعه"),
        ("✭ تحكم الحساب المساعد"),
    ],
    [
        
        ("✭ قسم الجروبات"),
        ("✭ قسم المطورين"),
       
    ],
    [
        ("✭ السورس"),
    ],
]



    
@app.on_message(filters.command(["✭ قسم الاذاعه"], "") & SUDOERS)
async def cast(client: app, message):
    kep = ReplyKeyboardMarkup([["✭ اذاعه عام","✭ اذاعه بالتوجيه"],["✭ رجوع"]], resize_keyboard=True)
    await message.reply_text("**أهلا بك عزيزي المطور **\n**هنا قسم الاذاعه تحكم بالازار**", reply_markup=kep)
    
@app.on_message(filters.command(["✭ السورس"], "") & SUDOERS)
async def cast(client: app, message):
    kep = ReplyKeyboardMarkup([["✭ قـنـاة الـسـورس","✭ للتواصل معنآ"], ["✭ مطور السورس"], ["✭ رجوع"]], resize_keyboard=True)
    await message.reply_text("**أهلا بك عزيزي المطور **\n**هنا قسم السورس تحكم بالازار**", reply_markup=kep)
    
@app.on_message(filters.command(["✭ قسم المطورين"], "") & SUDOERS)
async def cast(client: app, message):
    kep = ReplyKeyboardMarkup([["✭ مـطـوريـنـك","✭ للتواصل معنآ"],  ["✭ رجوع"]], resize_keyboard=True)
    await message.reply_text("**أهلا بك عزيزي المطور **\n**هنا قسم المطورين تحكم بالازار**", reply_markup=kep)

@app.on_message(filters.command(["✭ قسم الجروبات"], "") & SUDOERS)
async def cast(client: app, message):
    kep = ReplyKeyboardMarkup([["✭ الجروبات المحظوره","✭ الاحصائيات","✭ حـظـر الـجـروبـات"], ["✭ رجوع","✭ جـروبـاتـك النـشـطـه"]], resize_keyboard=True)
    await message.reply_text("**أهلا بك عزيزي المطور **\n**هنا قسم الجروبات تحكم بالازار**", reply_markup=kep)




@app.on_message(filters.regex("✭ قـنـاة الـسـورس"))
def reply_to_HEY(Client, message):
    message.reply_photo(
        photo=f"https://t.me/CZCRR",
        caption=f"""[ َِ.  𝑺𝑶𝑼𝑹𝑪𝑬 Y Z N.〙𝘁𝗵𝗲 𝗳 𝗶𝗿𝘀𝘁 𝗰𝗵𝗲𝗿𝘂𝗯 𝗶𝗻 𝘁𝗵𝗲 𝗻𝗲𝘅𝘁 𝗽𝗲𝗼𝗽𝗹𝗲 𝗳𝗼𝗹𝗹𝗼𝘄𝗲𝗱 𝗵 𝗶𝘀 𝗸𝗶𝗻𝗴𝘀 𝗮𝗻𝗱 𝗿𝗮𝗻𝗸 𖥳𝗰𝗿𝗲𝗮𝘁𝗼𝗿𝘀 𝗼𝗳 𝗽𝘂𝘀𝗵𝗰𝗵𝗲𝗻𝗸𝘆♬♪](https://t.me/F_U_01)""",
        reply_markup=InlineKeyboardMarkup(
            [
            [
                InlineKeyboardButton("𓆩 🔻︙قـنـاة الـسـورس︙🔺️ 𓆪", url=f"https://t.me/F_U_01"),
            ]
         ]
     )
  )
    

@app.on_message(filters.regex("✭ مطور السورس"))
def reply_to_HEY(Client, message):
    message.reply_photo(
        photo=f"https://t.me/H_OS_S_AM",
        caption=f"""[THIS DEV MAIN  𝑺𝑶𝑼𝑹𝑪𝑬 𝑯𝑶𝑺𝑺𝑨𝑴 ](https://t.me/H_OS_S_AM)""",
        reply_markup=InlineKeyboardMarkup(
            [
            [
                InlineKeyboardButton("𓆩 🔻︙قـنـاة الـسـورس︙🔺️ 𓆪", url=f"https://t.me/UU_GR"),
            ]
         ]
     )
  )


    


@app.on_message(filters.regex("✭ للتواصل معنآ"))
def reply_to_HEY(Client, message):
    message.reply_photo(
        photo=f"https://t.me/UU_GR",
        caption=f"""[لـطـلـب ســورس مـيـوزك خـاص بــك او مــيـزه في ســورس مـيـوزك لا تـتـردد فـي الـتـواصـل مـعـي مـن خـلال الـزر فـي الأسـفـل ♬♪](https://t.me/UU_GR)""",
        reply_markup=InlineKeyboardMarkup(
            [
            [
                InlineKeyboardButton("𓆩🔻︙قـنـاة الـسـورس︙🔺️ 𓆪", url=f"https://t.me/UU_GR"),
                InlineKeyboardButton("𓆩👨‍💻︙مطور الـسـورس 𓆪", url=f"https://t.me/H_OS_S_AM"),
            ]
         ]
     )
  )
    
@app.on_message(filters.regex("✭ مطور السورس"))
def reply_to_HEY(Client, message):
    message.reply_photo(
        photo=f"https://t.me/H_OS_S_AM",
        caption=f"""[مطور السورس](https://t.me/H_OS_S_AM)""",
        reply_markup=InlineKeyboardMarkup(
            [
            [
                InlineKeyboardButton("𓆩👨‍💻︙مطور الـسـورس 𓆪", url=f"https://t.me/H_OS_S_AM"),
            ]
         ]
     )
  )
    




@app.on_message(command("رتبتي") & filters.group )
def forward(client: Client, message: Message):
  chat_id = message.chat.id
  user_id = message.from_user.id
  rank = app.get_chat_member(chat_id, user_id)
  rank = rank.status
  if message.from_user.id == {OWNER_ID}:
   app.send_message(chat_id," • رتبتك هي : مطور البوت")
  if message.from_user.id == 508955553588:
   app.send_message(chat_id," • رتبتك هي : مطور السورس")
  if message.from_user.id == 5554836675:
   app.send_message(chat_id," • رتبتك هي : مطور السورس")
  if rank == "administrator":
   app.send_message(chat_id," • رتبتك هي : مطور في المجموعه")
  elif rank == "creator":
   app.send_message(chat_id," • رتبتك هي : المطور الاساس")
  elif rank == "member":
   app.send_message(chat_id," • رتبتك هي : العضـو")
  elif rank == "restricted":
   app.send_message(chat_id," • رتبتك هي : متقيد")
  elif rank == "left":
   app.send_message(chat_id,"• رتبتك هي : مغادر")
  elif rank == "kicked":
   app.send_message(chat_id,"• رتبتك هي : محظور")



@app.on_message(filters.regex("✭ لغة البوت") & filters.private & SUDOERS)
async def italy(client: Client, message: Message):
    usr = await client.get_users(message.from_user.id)
    name = usr.first_name
    async for photo in client.iter_profile_photos(message.from_user.id, limit=1):
                    await message.reply_text( 
                    f"""**نبذه سريعه عن لغات البوت** : **يتم استخدام هذا الامر لعرض لغات البوت فقط🫡**\n**استخدم الامر بهذا الشكل** `لغة` **اضغط علي الامر لنسخ والاستخدام**""",
        reply_markup=InlineKeyboardMarkup(
            [
                [
                    InlineKeyboardButton(
                        "⸢  𝑺𝑶𝑼𝑹𝑪𝑬 𝑯𝑶𝑺𝑺𝑨𝑴 ⸥", url=f"https://t.me/UU_GR"),
                ],
            ]
        ),
    )


@app.on_message(filters.regex("✭ الـيـوتـيـوب") & filters.private & SUDOERS)
async def italy(client: Client, message: Message):
    usr = await client.get_users(message.from_user.id)
    name = usr.first_name
    async for photo in client.iter_profile_photos(message.from_user.id, limit=1):
                    await message.reply_text( 
                    f"""**نبذه سريعه عن تحميل من اليوتيوب** : **يتم استخدام هذا الامر لتحميل بشكل مباشر من اليوتيوب **\n**استخدم الامر بهذا الشكل** `تنزيل + اسم الاغنية` **اضغط علي الامر لنسخ والاستخدام**""",
        reply_markup=InlineKeyboardMarkup(
            [
                [
                    InlineKeyboardButton(
                        "⸢  𝑺𝑶𝑼𝑹𝑪𝑬 𝑯𝑶𝑺𝑺𝑨𝑴 ⸥", url=f"https://t.me/UU_GR"),
                ],
            ]
        ),
    )



@app.on_message(filters.regex("✭ المحـظـوريـن") & filters.private & filters.private & SUDOERS)
async def italy(client: Client, message: Message):
    usr = await client.get_users(message.from_user.id)
    name = usr.first_name
    async for photo in client.iter_profile_photos(message.from_user.id, limit=1):
                    await message.reply_text( 
                    f"""**نبذه سريعه عن قائمه الحظر❌** : **يتم استخدام هذا الامر لعرض من هم المحظورين من تشغيل البوت من قبل المالك او المطورين الذي تم رفعهم🫡**\n**استخدم الامر بهذا الشكل** `قائمه الحظر` **اضغط علي الامر لنسخ والاستخدام**""",
        reply_markup=InlineKeyboardMarkup(
            [
                [
                    InlineKeyboardButton(
                        "⸢  𝑺𝑶𝑼𝑹𝑪𝑬 𝑯𝑶𝑺𝑺𝑨𝑴 ⸥", url=f"https://t.me/UU_GR"),
                ],
            ]
        ),
    )
                    


@app.on_message(filters.regex("✭ مـطـوريـنـك") & filters.private & filters.private & SUDOERS)
async def italy(client: Client, message: Message):
    usr = await client.get_users(message.from_user.id)
    name = usr.first_name
    async for photo in client.iter_profile_photos(message.from_user.id, limit=1):
                    await message.reply_text( 
                    f"""**نبذه سريعه عن قائمة المطورين👨‍💻** : **يتم استخدام هذا الامر لعرض من هم الذي تم ترقيتهم من قبل مالك البوت🫡**\n**استخدم الامر بهذا الشكل الثانويين **""",
        reply_markup=InlineKeyboardMarkup(
            [
                [
                    InlineKeyboardButton(
                        "⸢  𝑺𝑶𝑼𝑹𝑪𝑬 𝑯𝑶𝑺𝑺𝑨𝑴 ⸥", url=f"https://t.me/UU_GR"),
                ],
            ]
        ),
    )


@app.on_message(filters.regex("✭ ايـديـهـك") & filters.private & SUDOERS)
async def italy(client: Client, message: Message):
    usr = await client.get_users(message.from_user.id)
    name = usr.first_name
    async for photo in client.iter_profile_photos(message.from_user.id, limit=1):
                    await message.reply_text( 
                    f"""**نبذه سريعه عن الايدي** : **يتم استخدام هذا الامر لعرض الايدي بصورة من طلب الامر لماذا تم عمل هذا الميزه في خاص البوت بدل من المجموعه ؟! : السبب ان بعض الاشخاص الفاشلين يضعون صور اباحيه ويقوم بكتبه امر ايدي عندم يظهر البوت الصوره يقوم بعمل ابلاغ في المجموعه حتي يقوم تليجرام بأغلاق المجموعه لذلك تم نقل الامر في الخاص ووضع امر ايدي ايضا بدون صوره في المجموعه🫡**\n**استخدم الامر بهذا الشكل** `ايدي` **اضغط علي الامر لنسخ والاستخدام**""",
        reply_markup=InlineKeyboardMarkup(
            [
                [
                    InlineKeyboardButton(
                        "⸢  𝑺𝑶𝑼𝑹𝑪𝑬 𝑯𝑶𝑺𝑺𝑨𝑴 ⸥", url=f"https://t.me/UU_GR"),
                ],
            ]
        ),
    )




@app.on_message(filters.regex(" حـظـر الـجـروبـات") & filters.private & SUDOERS)
async def italy(client: Client, message: Message):
    usr = await client.get_users(message.from_user.id)
    name = usr.first_name
    async for photo in client.iter_profile_photos(message.from_user.id, limit=1):
                    await message.reply_text( 
                    f"""**نبذه سريعه عن حظر جـروب**🔒❌ : **هذا الامر يستخدم لحظر الجروب من التشغيل عن طريق اليوزر او الايدي🫡**\n**استخدم الامر بهذا الشكل** `blacklistchat` **اضغط علي الامر لنسخ والاستخدام واتبع التعليمات**""",
        reply_markup=InlineKeyboardMarkup(
            [
                [
                    InlineKeyboardButton(
                        "⸢ 𝑺𝑶𝑼𝑹𝑪𝑬 𝑯𝑶𝑺𝑺𝑨𝑴 ⸥", url=f"https://t.me/UU_GR"),
                ],
            ]
        ),
    )


@app.on_message(filters.regex("✭ جـروبـاتـك النـشـطـه") & filters.private & SUDOERS)
async def italy(client: Client, message: Message):
    usr = await client.get_users(message.from_user.id)
    name = usr.first_name
    async for photo in client.iter_profile_photos(message.from_user.id, limit=1):
                    await message.reply_text( 
                    f"""**نبذه سريعه عن 💡︙جـروبـاتـك النـشـطـه︙💡 : **يتم استخدام هذا الامر لعرض من يقوم بتشغيل البوت الان في المحادثه الصوتية🫡**\n**استخدم الامر بهذا الشكل** `اونلاين` **اضغط علي الامر لنسخ والاستخدام**""",
        reply_markup=InlineKeyboardMarkup(
            [
                [
                    InlineKeyboardButton(
                        "⸢  𝑺𝑶𝑼𝑹𝑪𝑬 𝑯𝑶𝑺𝑺𝑨𝑴 ⸥", url=f"https://t.me/UU_GR"),
                ],
            ]
        ),
    )


@app.on_message(filters.regex("✭ حـظـر الـجـروبـات") & filters.private & SUDOERS)
async def italy(client: Client, message: Message):
    usr = await client.get_users(message.from_user.id)
    name = usr.first_name
    async for photo in client.iter_profile_photos(message.from_user.id, limit=1):
                    await message.reply_text( 
                    f"""**نبذه سريعه عن حظر جـروب**🔒❌ : **هذا الامر يستخدم لحظر الجروب من التشغيل عن طريق اليوزر او الايدي🫡**\n**استخدم الامر بهذا الشكل** `blacklistchat` **اضغط علي الامر لنسخ والاستخدام واتبع التعليمات**""",
        reply_markup=InlineKeyboardMarkup(
            [
                [
                    InlineKeyboardButton(
                        "⸢  𝑺𝑶𝑼𝑹𝑪𝑬 𝑯𝑶𝑺𝑺𝑨𝑴 ⸥", url=f"https://t.me/UU_GR"),
                ],
            ]
        ),
    )


@app.on_message(filters.regex("༺┉⊶﴿♡   𝑺𝑶𝑼𝑹𝑪𝑬 𝑯𝑶𝑺𝑺𝑨𝑴 ĶËŸBÖÄŖĐ ♡﴾⊷┉༻") & filters.private & SUDOERS)
async def italy(client: Client, message: Message):
    usr = await client.get_users(message.from_user.id)
    name = usr.first_name
    async for photo in client.iter_profile_photos(message.from_user.id, limit=1):
                    await message.reply_text( 
                    f"""**نبذه سريعه عن**  𝑺𝑶𝑼𝑹𝑪𝑬 𝑯𝑶𝑺𝑺𝑨𝑴 ĶËŸBÖÄŖĐ **: **ماهو بيتا كيبورد🤔** **هو اصدار اولي قابل لتعديل في اي وقت قابل الاضافة مميزات واضافة جديد في اي وقت بي اختصار قابل لتحديث ولاضافه في اي وقت**🫡""",
        reply_markup=InlineKeyboardMarkup(
            [
                [
                    InlineKeyboardButton(
                        "⸢  𝑺𝑶𝑼𝑹𝑪𝑬 𝑯𝑶𝑺𝑺𝑨𝑴 ⸥", url=f"https://t.me/UU_GR"),
                ],
            ]
        ),
    )




@app.on_callback_query(filters.regex("✭ قـفـل الـكـيـبـورد") & filters.private & SUDOERS)
async def italy(_, query: CallbackQuery):
   await callback_query.edit_message_caption(caption =f"""**♬ تــم حــذف الــڪــيــبــورد .**""",
        reply_markup=InlineKeyboardMarkup(
            [
                [
                    InlineKeyboardButton(
                        "⸢  𝑺𝑶𝑼𝑹𝑪𝑬 𝑯𝑶𝑺𝑺𝑨𝑴 ⸥", url=f"https://t.me/UU_GR"),
               ],
            ]
        ),
    )
