import logging
from pyrogram import Client, filters, enums
from pyrogram.types import (
    Message,
    InlineKeyboardButton,
    InlineKeyboardMarkup,
    CallbackQuery,
)
from pyrogram.errors import (
    FloodWait,
    InputUserDeactivated,
    UserIsBlocked,
    UserNotParticipant,
    MessageTooLong,
    PeerIdInvalid,
)
from Script import script

@Client.on_callback_query()
async def cb_handler(client: Client, query: CallbackQuery):
    if query.data == "close_data":
        try:
            user = query.message.reply_to_message.from_user.id
        except:
            user = query.from_user.id
        if int(user) != 0 and query.from_user.id != int(user):
            return await query.answer(script.ALRT_TXT, show_alert=True)
        await query.answer("ᴛʜᴀɴᴋs ꜰᴏʀ ᴄʟᴏsᴇ ")
        await query.message.delete()
        try:
            await query.message.reply_to_message.delete()
        except:
            pass

    elif query.data == "about":
        await query.message.edit_text(text="● ◌ ◌")
        await query.message.edit_text(text="● ● ◌")
        await query.message.edit_text(text="● ● ●")

        features_keyboard = InlineKeyboardMarkup(
            [
                [InlineKeyboardButton("‼️ ᴅɪꜱᴄʟᴀɪᴍᴇʀ ‼️", callback_data="disclaimer")],
                [
                    InlineKeyboardButton(
                        "• ᴠɪsɪᴛ ᴏᴜʀ ᴄᴏᴍᴍᴜɴɪᴛʏ •", url="t.me/SPIDEYOFFICIAL_777"
                    )
                ],
                [
                    InlineKeyboardButton("• ᴏᴡɴᴇʀ •", user_id=int(7965267063)),
                    InlineKeyboardButton("• sᴏᴜʀᴄᴇ •", callback_data="source"),
                ],
                [InlineKeyboardButton("🛰️ ʀᴇɴᴅᴇʀɪɴɢ ꜱᴛᴀᴛᴜꜱ ☁️", callback_data="rendr")],
                [InlineKeyboardButton("⋞ Back ᴛᴏ ʜᴏᴍᴇ ", callback_data="back")],
            ]
        )

        await query.message.edit_text(
            script.ABOUT_TXT, reply_markup=features_keyboard
        )

    elif query.data == "feedback_feature":
        await query.answer(
            "🛠️ Feedback: Save and display user feedback for admins seamlessly!",
            show_alert=True,
        )

    elif query.data == "disclaimer":
        disclaimer_keyboard = InlineKeyboardMarkup(
            [
                [
                    InlineKeyboardButton(
                        "📲 ᴄᴏɴᴛᴀᴄᴛ ᴛᴏ ᴏᴡɴᴇʀ", url="https://t.me/hacker_x_official_777"
                    )
                ],
                [InlineKeyboardButton("⪻ ʙᴀᴄᴋ", callback_data="about")],
            ]
        )

        await query.message.edit_text(text="● ◌ ◌")
        await query.message.edit_text(text="● ● ◌")
        await query.message.edit_text(text="● ● ●")

        await query.message.edit_text(
            script.DISCLAIMER_TXT, reply_markup=disclaimer_keyboard
        )

    elif query.data == "back":
        await query.message.edit_text(text="● ◌ ◌")
        await query.message.edit_text(text="● ● ◌")
        await query.message.edit_text(text="● ● ●")

        welcome_message = script.START_MSG.format(query.from_user.mention, get_status())

        main_keyboard = InlineKeyboardMarkup(
            [
                [
                    InlineKeyboardButton(
                    "➕ Aᴅᴅ Mᴇ ᴛᴏ Yᴏᴜʀ Cʜᴀɴɴᴇʟ ➕",
                    url="https://t.me/SPIDER_MAN_GAMING_bot?startchannel=Bots4Sale&admin=invite_users+manage_chat",
                )
                ],
                [
                    InlineKeyboardButton("🚀 Channel", url="https://t.me/SPIDEYOFFICIAL_777"),
                    InlineKeyboardButton("💬 Sᴜᴘᴘᴏʀᴛ", callback_data="group_info"),
            ],
            [
                    InlineKeyboardButton("ℹ️ Aʙᴏᴜᴛ", callback_data="about"),
                InlineKeyboardButton("📃 Features", callback_data="features"),
                ],
                [
                    InlineKeyboardButton(
                    "➕ Aᴅᴅ Mᴇ ᴛᴏ Yᴏᴜʀ Gʀᴏᴜᴘ ➕",
                    url="https://t.me/SPIDER_MAN_GAMING_bot?startgroup=true",
                )
            ],
        ]
    )

    # Final message
        await query.message.edit_text(
        welcome_message,     reply_markup=main_keyboard
    )


    elif query.data == "group_info":
        await query.message.edit_text(text="● ◌ ◌")
        await query.message.edit_text(text="● ● ◌")
        await query.message.edit_text(text="● ● ●")

        buttons = [
            [
                InlineKeyboardButton(
                    "× ᴀʟʟ ᴏᴜʀ ʟɪɴᴋꜱ ×", url="https://t.me/SPIDEYOFFICIAL777"
                )
            ],
            [
                InlineKeyboardButton("• ᴍᴏᴠɪᴇ ɢʀᴏᴜᴘ •", url="https://t.me/+KTXnXf_YPxJlOGRl"),
                InlineKeyboardButton(
                    "• ᴜᴘᴅᴀᴛᴇs •", url="https://t.me/SpideyOfficialUpdatez"
                ),
            ],
            [
                InlineKeyboardButton("• ʜᴀᴄᴋ •", url="https://t.me/+cMlrPqMjUwtmNTI1"),
                InlineKeyboardButton(
                    "• 𝟷𝟾+ 🚫 •", url="https://t.me/movie_flex_official"
                ),
            ],
            [
                InlineKeyboardButton(
                    "• ᴄɪɴᴇғʟɪx •", url="https://t.me/+QVmLP_hlHNw3M2I1"
                )
            ],
            [InlineKeyboardButton("⪻ ʙᴀᴄᴋ •", callback_data="back")],
        ]

        reply_markup = InlineKeyboardMarkup(buttons)

        await query.message.edit_text(
            text=script.CHANNELS.format(query.from_user.mention),
            reply_markup=reply_markup,
            parse_mode=enums.ParseMode.HTML,
        )

    elif query.data == "rendr":
        await query.answer(script.ALERT_MSG, show_alert=True)

    elif query.data == "source":
        await query.message.edit_text(text="● ◌ ◌")
        await query.message.edit_text(text="● ● ◌")
        await query.message.edit_text(text="● ● ●")

        buttons = [
        [
                InlineKeyboardButton("⪻ ʙᴀᴄᴋ", callback_data="about"),
                InlineKeyboardButton("sᴜᴘᴘᴏʀᴛ", callback_data="group_info"),
        ]
    ]

        reply_markup = InlineKeyboardMarkup(buttons)


        await query.message.edit_text(
            text=script.SOURCE_TXT.format(
                query.from_user.mention if query.from_user else "User"
            ),
            reply_markup=reply_markup,
            parse_mode=enums.ParseMode.HTML,
            )



    elif query.data == "spidey":
        await query.message.edit_text(text="● ◌ ◌")
        await query.message.edit_text(text="● ● ◌")
        await query.message.edit_text(text="● ● ●")

        buttons = [
            [
                InlineKeyboardButton("⪻ ʙᴀᴄᴋ", callback_data="features"),
                InlineKeyboardButton("sᴜᴘᴘᴏʀᴛ", callback_data="group_info"),
        ]
    ]

        reply_markup = InlineKeyboardMarkup(buttons)

        await query.message.edit_text(
            text=script.OWNER_TEXT,
            reply_markup=reply_markup,
            parse_mode=enums.ParseMode.HTML,
    )