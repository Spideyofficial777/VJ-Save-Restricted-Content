import os
import asyncio 
import pyrogram
from pyrogram import Client, filters, enums
from pyrogram.errors import FloodWait, UserIsBlocked, InputUserDeactivated, UserAlreadyParticipant, InviteHashExpired, UsernameNotOccupied
from pyrogram.types import InlineKeyboardMarkup, InlineKeyboardButton, Message 
from config import * # API_ID, API_HASH, ERROR_MESSAGE
from database.db import db
from Spidey.strings import HELP_TXT
from Script import script
from pyrogram.errors import UserNotParticipant
from database.db import * # get_all_users, add_user, already_db
from utils import* #

class batch_temp(object):
    IS_BATCH = {}

async def downstatus(client, statusfile, message, chat):
    while True:
        if os.path.exists(statusfile):
            break

        await asyncio.sleep(3)
      
    while os.path.exists(statusfile):
        with open(statusfile, "r") as downread:
            txt = downread.read()
        try:
            await client.edit_message_text(chat, message.id, f"**Downloaded:** **{txt}**")
            await asyncio.sleep(10)
        except:
            await asyncio.sleep(5)


# upload status
async def upstatus(client, statusfile, message, chat):
    while True:
        if os.path.exists(statusfile):
            break

        await asyncio.sleep(3)      
    while os.path.exists(statusfile):
        with open(statusfile, "r") as upread:
            txt = upread.read()
        try:
            await client.edit_message_text(chat, message.id, f"**Uploaded:** **{txt}**")
            await asyncio.sleep(10)
        except:
            await asyncio.sleep(5)


# progress writer
def progress(current, total, message, type):
    with open(f'{message.id}{type}status.txt', "w") as fileup:
        fileup.write(f"{current * 100 / total:.1f}%")

welcome_image = "https://envs.sh/v3t.jpg"

# start command
@Client.on_message(filters.command("start"))
async def start(client, message):
    try:
        if temp.U_NAME is None:
            temp.U_NAME = (await client.get_me()).username
        if temp.B_NAME is None:
            temp.B_NAME = (await client.get_me()).first_name  

    except Exception as e:
        print(f"Error fetching bot details: {e}")  

    user_id = message.from_user.id
    user_name = message.from_user.first_name

    is_new = False
    if not already_db(user_id):
        add_user(user_id, user_name)
        is_new = True

    if is_new:
        from datetime import datetime
        Spidey = script.NEW_USER_LOG.format(
            bot_name=temp.B_NAME,
            user_id=user_id,
            user_mention=message.from_user.mention,
            username=f"@{message.from_user.username}" if message.from_user.username else "None",
            chat_title=message.chat.title if message.chat.type in [enums.ChatType.GROUP, enums.ChatType.SUPERGROUP] else "Private Chat",
            time=datetime.now().strftime("%d-%b-%Y %I:%M %p")
        )
        await client.send_message(LOG_CHANNEL, Spidey)

    if message.chat.type in [enums.ChatType.GROUP, enums.ChatType.SUPERGROUP]:
        buttons = [
            [InlineKeyboardButton('• ᴀᴅᴅ ᴍᴇ ᴛᴏ ᴜʀ ᴄʜᴀᴛ •', url=f'http://t.me/{temp.U_NAME}?startgroup=true')],
            [
                InlineKeyboardButton('• ᴍᴀsᴛᴇʀ •', url="https://t.me/hacker_x_official_777"),
                InlineKeyboardButton('• sᴜᴘᴘᴏʀᴛ •', url='https://t.me/deathchatting_world')
            ],
            [InlineKeyboardButton('• ᴊᴏɪɴ ᴜᴘᴅᴀᴛᴇs ᴄʜᴀɴɴᴇʟ •', url="https://t.me/+9tdbATrOMLNlN2I1")]
        ]
        reply_markup = InlineKeyboardMarkup(buttons)
        await message.reply(script.GSTART_TXT.format(message.from_user.mention, temp.U_NAME, temp.B_NAME), reply_markup=reply_markup)
        return  

    try:
        for channel in CHANNEL_IDS:
            try:
                await client.get_chat_member(channel, message.from_user.id)
            except UserNotParticipant:
                raise UserNotParticipant 
        
        import random
        
        welcome_image_url = random.choice(START_IMG)

        m = await message.reply_text("<b>ʜᴇʟʟᴏ ʙᴀʙʏ, ʜᴏᴡ ᴀʀᴇ ʏᴏᴜ \nᴡᴀɪᴛ ᴀ ᴍᴏᴍᴇɴᴛ ʙᴀʙʏ ....</b>")
        await asyncio.sleep(0.4)
        await m.edit_text("🎊")
        await asyncio.sleep(0.5)
        await m.edit_text("⚡")
        await asyncio.sleep(0.5)
        await m.edit_text("<b>ꜱᴛᴀʀᴛɪɴɢ ʙᴀʙʏ...</b>")
        await asyncio.sleep(0.4)
        await m.delete()

        m = await message.reply_sticker("CAACAgUAAxkBAAIdBGd7qZ7kMBTPT2YAAdnPRDtBSw9jwAACqwQAAr7vuFdHULNVi6H4nB4E")
        await asyncio.sleep(3)
        await m.delete()

        keyboard = InlineKeyboardMarkup(
            [
                [InlineKeyboardButton("➕ Aᴅᴅ Mᴇ ᴛᴏ Yᴏᴜʀ Cʜᴀɴɴᴇʟ ➕", url="https://t.me/SPIDER_MAN_GAMING_bot?startchannel=Bots4Sale&admin=invite_users+manage_chat")],
                [InlineKeyboardButton("🚀 Cʜᴀɴɴᴇʟ", url="https://t.me/+cMlrPqMjUwtmNTI1"),
                 InlineKeyboardButton("💬 Sᴜᴘᴘᴏʀᴛ", callback_data="group_info")],
                [InlineKeyboardButton("ℹ️ Aʙᴏᴜᴛ", callback_data="about"),
                 InlineKeyboardButton("📃 Fᴇᴀᴛᴜʀᴇs", callback_data="features")],
                [InlineKeyboardButton("➕  Aᴅᴅ Mᴇ ᴛᴏ Yᴏᴜʀ Gʀᴏᴜᴘ ➕", url="https://t.me/SPIDER_MAN_GAMING_bot?startgroup=true")]
            ]
        )

        await message.reply_photo(
            photo=welcome_image_url,
            caption=script.START_MSG.format(message.from_user.mention, get_status()),
            reply_markup=keyboard,
)


    except UserNotParticipant:
        import random
        buttons = []
        for channel in CHANNEL_IDS:
            try:
                chat = await client.get_chat(channel)  
                if chat.username:
                    channel_link = f"https://t.me/{chat.username}"
                else:
                    channel_link = await client.export_chat_invite_link(channel) 

                buttons.append([InlineKeyboardButton(f"🚀 Join {chat.title}", url=channel_link)])

            except Exception as e:
                print(f"Error fetching channel link: {e}")  
                continue 

        buttons.append([InlineKeyboardButton("🔄 ᴄʜᴇᴄᴋ ᴀɢᴀɪɴ", callback_data="chk")])
        keyboard = InlineKeyboardMarkup(buttons)

        await message.reply_photo(
            photo=welcome_image,
            caption=f"<b>⚠️ Access Denied! ⚠️\n\n🔥 Hello {message.from_user.mention}!\n\n"
                    "You need to join all required channels before proceeding!\n\n"
                    "👉 [✨ Join Now ✨](https://t.me/SPIDEYOFFICIAL777)</b>",
            reply_markup=keyboard
        )


@Client.on_callback_query(filters.regex("chk"))
async def check_subscription(client, callback_query: CallbackQuery):
    try:
        missing_channels = []

        for channel in CHANNEL_IDS:
            try:
                await client.get_chat_member(channel, callback_query.from_user.id)
            except UserNotParticipant:
                missing_channels.append(channel)

        if not missing_channels:
            keyboard = InlineKeyboardMarkup([
                [InlineKeyboardButton("➕ Aᴅᴅ Mᴇ ᴛᴏ Yᴏᴜʀ Cʜᴀɴɴᴇʟ ➕",
                    url="https://t.me/SPIDER_MAN_GAMING_bot?startchannel=Bots4Sale&admin=invite_users+manage_chat")],
                [InlineKeyboardButton("🚀 Cʜᴀɴɴᴇʟ", url="https://t.me/+cMlrPqMjUwtmNTI1"),
                 InlineKeyboardButton("💬 Sᴜᴘᴘᴏʀᴛ", url="https://t.me/SPIDEYOFFICIAL777")],
                [InlineKeyboardButton("➕ Aᴅᴅ Mᴇ ᴛᴏ Yᴏᴜʀ Gʀᴏᴜᴘ ➕",
                    url="https://t.me/SPIDER_MAN_GAMING_bot?startgroup=true")]
            ])

            await callback_query.message.edit_text(
                script.START_MSG.format(callback_query.from_user.mention, get_status()),
                reply_markup=keyboard,
                disable_web_page_preview=True
            )
        else:
            # Show only missing channels
            buttons = []
            for channel in missing_channels:
                try:
                    chat = await client.get_chat(channel)
                    name = chat.title or "Channel"
                    link = f"https://t.me/{chat.username}" if chat.username else await client.export_chat_invite_link(channel)
                    buttons.append([InlineKeyboardButton(f"🚀 Join {name}", url=link)])
                except Exception as e:
                    print(f"Error fetching channel info: {e}")
                    continue

            buttons.append([InlineKeyboardButton("🔄 ᴄʜᴇᴄᴋ ᴀɢᴀɪɴ", callback_data="chk")])
            keyboard = InlineKeyboardMarkup(buttons)

            await callback_query.answer(
                "🙅 Yᴏᴜ ᴀʀᴇ ɴᴏᴛ sᴜʙsᴄʀɪʙᴇᴅ ᴛᴏ ᴀʟʟ ʀᴇǫᴜɪʀᴇᴅ ᴄʜᴀɴɴᴇʟs. Jᴏɪɴ ᴀɴᴅ ᴛᴀᴘ 'Cʜᴇᴄᴋ Aɢᴀɪɴ' 🙅",
                show_alert=True
            )
            await callback_query.message.edit_text(
                "🔔 Jᴏɪɴ ᴛʜᴇsᴇ ᴄʜᴀɴɴᴇʟs ᴛᴏ ᴄᴏɴᴛɪɴᴜᴇ:",
                reply_markup=keyboard
            )

    except Exception as e:
        print(f"Unexpected error: {e}")


            


# help command
@Client.on_message(filters.command(["help"]))
async def send_help(client: Client, message: Message):
    await client.send_message(
        chat_id=message.chat.id, 
        text=f"{HELP_TXT}"
    )

# cancel command
@Client.on_message(filters.command(["cancel"]))
async def send_cancel(client: Client, message: Message):
    batch_temp.IS_BATCH[message.from_user.id] = True
    await client.send_message(
        chat_id=message.chat.id, 
        text="**Batch Successfully Cancelled.**"
    )

@Client.on_message(filters.text & filters.private)
async def save(client: Client, message: Message):
    if "https://t.me/" in message.text:
        if batch_temp.IS_BATCH.get(message.from_user.id) == False:
            return await message.reply_text("**One Task Is Already Processing. Wait For Complete It. If You Want To Cancel This Task Then Use - /cancel**")
        datas = message.text.split("/")
        temp = datas[-1].replace("?single","").split("-")
        fromID = int(temp[0].strip())
        try:
            toID = int(temp[1].strip())
        except:
            toID = fromID
        batch_temp.IS_BATCH[message.from_user.id] = False
        for msgid in range(fromID, toID+1):
            if batch_temp.IS_BATCH.get(message.from_user.id): break
            user_data = await db.get_session(message.from_user.id)
            if user_data is None:
                await message.reply("**For Downloading Restricted Content You Have To /login First.**")
                batch_temp.IS_BATCH[message.from_user.id] = True
                return
            try:
                acc = Client("saverestricted", session_string=user_data, api_hash=API_HASH, api_id=API_ID)
                await acc.connect()
            except:
                batch_temp.IS_BATCH[message.from_user.id] = True
                return await message.reply("**Your Login Session Expired. So /logout First Then Login Again By - /login**")
            
            # private
            if "https://t.me/c/" in message.text:
                chatid = int("-100" + datas[4])
                try:
                    await handle_private(client, acc, message, chatid, msgid)
                except Exception as e:
                    if ERROR_MESSAGE == True:
                        await client.send_message(message.chat.id, f"Error: {e}", reply_to_message_id=message.id)
    
            # bot
            elif "https://t.me/b/" in message.text:
                username = datas[4]
                try:
                    await handle_private(client, acc, message, username, msgid)
                except Exception as e:
                    if ERROR_MESSAGE == True:
                        await client.send_message(message.chat.id, f"Error: {e}", reply_to_message_id=message.id)
            
            # public
            else:
                username = datas[3]

                try:
                    msg = await client.get_messages(username, msgid)
                except UsernameNotOccupied: 
                    await client.send_message(message.chat.id, "The username is not occupied by anyone", reply_to_message_id=message.id)
                    return
                try:
                    await client.copy_message(message.chat.id, msg.chat.id, msg.id, reply_to_message_id=message.id)
                except:
                    try:    
                        await handle_private(client, acc, message, username, msgid)               
                    except Exception as e:
                        if ERROR_MESSAGE == True:
                            await client.send_message(message.chat.id, f"Error: {e}", reply_to_message_id=message.id)

            # wait time
            await asyncio.sleep(3)
        batch_temp.IS_BATCH[message.from_user.id] = True


# handle private
async def handle_private(client: Client, acc, message: Message, chatid: int, msgid: int):
    msg: Message = await acc.get_messages(chatid, msgid)
    if msg.empty: return 
    msg_type = get_message_type(msg)
    if not msg_type: return 
    chat = message.chat.id
    if batch_temp.IS_BATCH.get(message.from_user.id): return 
    if "Text" == msg_type:
        try:
            await client.send_message(chat, msg.text, entities=msg.entities, reply_to_message_id=message.id, parse_mode=enums.ParseMode.HTML)
            return 
        except Exception as e:
            if ERROR_MESSAGE == True:
                await client.send_message(message.chat.id, f"Error: {e}", reply_to_message_id=message.id, parse_mode=enums.ParseMode.HTML)
            return 

    smsg = await client.send_message(message.chat.id, '**Downloading**', reply_to_message_id=message.id)
    asyncio.create_task(downstatus(client, f'{message.id}downstatus.txt', smsg, chat))
    try:
        file = await acc.download_media(msg, progress=progress, progress_args=[message,"down"])
        os.remove(f'{message.id}downstatus.txt')
    except Exception as e:
        if ERROR_MESSAGE == True:
            await client.send_message(message.chat.id, f"Error: {e}", reply_to_message_id=message.id, parse_mode=enums.ParseMode.HTML) 
        return await smsg.delete()
    if batch_temp.IS_BATCH.get(message.from_user.id): return 
    asyncio.create_task(upstatus(client, f'{message.id}upstatus.txt', smsg, chat))

    if msg.caption:
        caption = msg.caption
    else:
        caption = None
    if batch_temp.IS_BATCH.get(message.from_user.id): return 
            
    if "Document" == msg_type:
        try:
            ph_path = await acc.download_media(msg.document.thumbs[0].file_id)
        except:
            ph_path = None
        
        try:
            await client.send_document(chat, file, thumb=ph_path, caption=caption, reply_to_message_id=message.id, parse_mode=enums.ParseMode.HTML, progress=progress, progress_args=[message,"up"])
        except Exception as e:
            if ERROR_MESSAGE == True:
                await client.send_message(message.chat.id, f"Error: {e}", reply_to_message_id=message.id, parse_mode=enums.ParseMode.HTML)
        if ph_path != None: os.remove(ph_path)
        

    elif "Video" == msg_type:
        try:
            ph_path = await acc.download_media(msg.video.thumbs[0].file_id)
        except:
            ph_path = None
        
        try:
            await client.send_video(chat, file, duration=msg.video.duration, width=msg.video.width, height=msg.video.height, thumb=ph_path, caption=caption, reply_to_message_id=message.id, parse_mode=enums.ParseMode.HTML, progress=progress, progress_args=[message,"up"])
        except Exception as e:
            if ERROR_MESSAGE == True:
                await client.send_message(message.chat.id, f"Error: {e}", reply_to_message_id=message.id, parse_mode=enums.ParseMode.HTML)
        if ph_path != None: os.remove(ph_path)

    elif "Animation" == msg_type:
        try:
            await client.send_animation(chat, file, reply_to_message_id=message.id, parse_mode=enums.ParseMode.HTML)
        except Exception as e:
            if ERROR_MESSAGE == True:
                await client.send_message(message.chat.id, f"Error: {e}", reply_to_message_id=message.id, parse_mode=enums.ParseMode.HTML)
        
    elif "Sticker" == msg_type:
        try:
            await client.send_sticker(chat, file, reply_to_message_id=message.id, parse_mode=enums.ParseMode.HTML)
        except Exception as e:
            if ERROR_MESSAGE == True:
                await client.send_message(message.chat.id, f"Error: {e}", reply_to_message_id=message.id, parse_mode=enums.ParseMode.HTML)     

    elif "Voice" == msg_type:
        try:
            await client.send_voice(chat, file, caption=caption, caption_entities=msg.caption_entities, reply_to_message_id=message.id, parse_mode=enums.ParseMode.HTML, progress=progress, progress_args=[message,"up"])
        except Exception as e:
            if ERROR_MESSAGE == True:
                await client.send_message(message.chat.id, f"Error: {e}", reply_to_message_id=message.id, parse_mode=enums.ParseMode.HTML)

    elif "Audio" == msg_type:
        try:
            ph_path = await acc.download_media(msg.audio.thumbs[0].file_id)
        except:
            ph_path = None

        try:
            await client.send_audio(chat, file, thumb=ph_path, caption=caption, reply_to_message_id=message.id, parse_mode=enums.ParseMode.HTML, progress=progress, progress_args=[message,"up"])   
        except Exception as e:
            if ERROR_MESSAGE == True:
                await client.send_message(message.chat.id, f"Error: {e}", reply_to_message_id=message.id, parse_mode=enums.ParseMode.HTML)
        
        if ph_path != None: os.remove(ph_path)

    elif "Photo" == msg_type:
        try:
            await client.send_photo(chat, file, caption=caption, reply_to_message_id=message.id, parse_mode=enums.ParseMode.HTML)
        except:
            if ERROR_MESSAGE == True:
                await client.send_message(message.chat.id, f"Error: {e}", reply_to_message_id=message.id, parse_mode=enums.ParseMode.HTML)
    
    if os.path.exists(f'{message.id}upstatus.txt'): 
        os.remove(f'{message.id}upstatus.txt')
        os.remove(file)
    await client.delete_messages(message.chat.id,[smsg.id])


# get the type of message
def get_message_type(msg: pyrogram.types.messages_and_media.message.Message):
    try:
        msg.document.file_id
        return "Document"
    except:
        pass

    try:
        msg.video.file_id
        return "Video"
    except:
        pass

    try:
        msg.animation.file_id
        return "Animation"
    except:
        pass

    try:
        msg.sticker.file_id
        return "Sticker"
    except:
        pass

    try:
        msg.voice.file_id
        return "Voice"
    except:
        pass

    try:
        msg.audio.file_id
        return "Audio"
    except:
        pass

    try:
        msg.photo.file_id
        return "Photo"
    except:
        pass

    try:
        msg.text
        return "Text"
    except:
        pass
        
