# Don't Remove Credit Tg - @VJ_Botz
# Subscribe YouTube Channel For Amazing Bot https://youtube.com/@Tech_VJ
# Ask Doubt on telegram @KingVJ01

import traceback
from pyrogram.types import Message
from pyrogram import Client, filters
from asyncio.exceptions import TimeoutError
from pyrogram.types import InlineKeyboardMarkup, InlineKeyboardButton
from pyrogram.errors import (
    ApiIdInvalid,
    PhoneNumberInvalid,
    PhoneCodeInvalid,
    PhoneCodeExpired,
    SessionPasswordNeeded,
    PasswordHashInvalid
)
from config import API_ID, API_HASH
from database.db import db

SESSION_STRING_SIZE = 351

@Client.on_message(filters.private & ~filters.forwarded & filters.command("logout"))
async def logout_handler(client: Client, message: Message):
    user_id = message.from_user.id

    try:
        # Check if session exists
        user_data = await db.get_session(user_id)
        if not user_data:
            return await message.reply("⚠️ <b>You are not logged in yet.</b>\nUse /login to log in.")

        # Remove session
        await db.set_session(user_id, session=None)

        return await message.reply("✅ <b>You have been logged out successfully!</b>\nUse /login again anytime.")
    
    except Exception as e:
        return await message.reply(f"❌ <b>Error while logging out:</b>\n<code>{e}</code>")

@Client.on_message(filters.private & ~filters.forwarded & filters.command("login"))
async def login_handler(bot: Client, message: Message):
    user_id = message.from_user.id

    # Check existing session
    user_data = await db.get_session(user_id)
    if user_data:
        return await message.reply("**You are already logged in! Please /logout before logging in again.**")

    try:
        # Step 1: Ask for phone number
        phone_number_msg = await bot.ask(
            chat_id=user_id,
            text="<b>Please enter your phone number with country code:</b>\n<code>+919876543210</code>\n\nSend /cancel to cancel.",
            filters=filters.text,
            timeout=300
        )
        if phone_number_msg.text.lower() == "/cancel":
            return await phone_number_msg.reply("❌ <b>Login process cancelled.</b>")

        phone_number = phone_number_msg.text
        client = Client(":memory:", api_id=API_ID, api_hash=API_HASH)
        await client.connect()

        # Step 2: Send OTP
        await phone_number_msg.reply("📨 Sending OTP...")
        try:
            code = await client.send_code(phone_number)
        except PhoneNumberInvalid:
            await client.disconnect()
            return await phone_number_msg.reply("❌ <b>Invalid phone number!</b>")
        
        # Step 3: Ask for OTP
        otp_msg = await bot.ask(
            user_id,
            "🔐 Please enter the OTP you received from Telegram.\n\nFormat: <code>1 2 3 4 5</code>\nSend /cancel to cancel.",
            filters=filters.text,
            timeout=300
        )
        if otp_msg.text.lower() == "/cancel":
            await client.disconnect()
            return await otp_msg.reply("❌ <b>Login process cancelled.</b>")

        phone_code = otp_msg.text.replace(" ", "")

        # Step 4: Sign in with OTP
        try:
            await client.sign_in(phone_number, code.phone_code_hash, phone_code)
        except PhoneCodeInvalid:
            await client.disconnect()
            return await otp_msg.reply("❌ <b>Invalid OTP!</b>")
        except PhoneCodeExpired:
            await client.disconnect()
            return await otp_msg.reply("❌ <b>OTP expired!</b>")
        except SessionPasswordNeeded:
            # Two-step password required
            password_msg = await bot.ask(
                user_id,
                "🔒 <b>Your account has 2-step verification enabled.</b>\nPlease enter your password.\nSend /cancel to cancel.",
                filters=filters.text,
                timeout=300
            )
            if password_msg.text.lower() == "/cancel":
                await client.disconnect()
                return await password_msg.reply("❌ <b>Login process cancelled.</b>")
            try:
                await client.check_password(password_msg.text)
            except PasswordHashInvalid:
                await client.disconnect()
                return await password_msg.reply("❌ <b>Invalid password!</b>")

        # Step 5: Export session string
        string_session = await client.export_session_string()
        await client.disconnect()

        if not string_session or len(string_session) < 100:
            return await message.reply("❌ <b>Session creation failed. Please try again.</b>")

        # Save session in DB
        await db.set_session(user_id, session=string_session)

        return await message.reply(
            "✅ <b>Your account has been logged in successfully!</b>\n\nIf you face any error related to <code>AUTH_KEY</code>, please /logout and /login again."
        )

    except Exception as e:
        return await message.reply(f"❌ <b>An unexpected error occurred:</b>\n<code>{str(e)}</code>")
