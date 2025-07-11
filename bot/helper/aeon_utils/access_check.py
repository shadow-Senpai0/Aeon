from time import time
from uuid import uuid4

from pyrogram.errors import PeerIdInvalid, RPCError, UserNotParticipant

from bot import (
    LOGGER,
    user_data,
)
from bot.core.aeon_client import TgClient
from bot.core.config_manager import Config
from bot.helper.aeon_utils.shorteners import short
from bot.helper.ext_utils.db_handler import database
from bot.helper.ext_utils.status_utils import get_readable_time
from bot.helper.telegram_helper.button_build import ButtonMaker


async def error_check(message):
    msg, button = [], None
    user = message.from_user or message.sender_chat
    user_id = user.id
    token_timeout = Config.TOKEN_TIMEOUT

    if Config.RSS_CHAT and user_id == int(Config.RSS_CHAT):
        return None, None

    if message.chat.type != message.chat.type.BOT:
        if FSUB_IDS := Config.FSUB_IDS:
            join_button = {}
            for channel_id in FSUB_IDS.split():
                chat = await get_chat_info(int(channel_id))
                if not chat:
                    continue

                try:
                    await chat.get_member(message.from_user.id)
                except UserNotParticipant:
                    invite_link = (
                        f"https://t.me/{chat.username}"
                        if chat.username
                        else chat.invite_link
                    )
                    join_button[chat.title] = invite_link
                except RPCError as e:
                    LOGGER.error(f"{e.NAME}: {e.MESSAGE} for {channel_id}")
                except Exception as e:
                    LOGGER.error(f"{e} for {channel_id}")

            if join_button:
                button = button or ButtonMaker()
                for title, link in join_button.items():
                    button.url_button(f"Join {title}", link, "footer")
                msg.append("You haven't joined our channel/group yet!")

        if not token_timeout or user_id in {
            Config.OWNER_ID,
            user_data.get(user_id, {}).get("SUDO"),
        }:
            try:
                temp_msg = await message._client.send_message(
                    chat_id=user_id,
                    text="<b>Checking Access...</b>",
                )
                await temp_msg.delete()
            except Exception:
                button = button or ButtonMaker()
                button.data_button("Start", f"aeon {user_id} private", "header")
                msg.append("You haven't initiated the bot in a private message!")

    if user_id not in {
        Config.OWNER_ID,
        Config.RSS_CHAT,
        user_data.get(user_id, {}).get("SUDO"),
    }:
        token_msg, button = await token_check(user_id, button)
        if token_msg:
            msg.append(token_msg)

    if msg:
        username = message.from_user.username
        tag = f"@{username}" if username else message.from_user.mention
        final_msg = f"Hey, <b>{tag}</b>!\n"
        for i, m in enumerate(msg, 1):
            final_msg += f"\n<blockquote><b>{i}</b>: {m}</blockquote>"

        if button:
            button = button.build_menu(2)
        return final_msg, button

    return None, None


async def get_chat_info(channel_id):
    try:
        return await TgClient.bot.get_chat(channel_id)
    except PeerIdInvalid as e:
        LOGGER.error(f"{e.NAME}: {e.MESSAGE} for {channel_id}")
        return None


async def check_is_paid(chat, uid):
    try:
        await chat.get_member(uid)
        return True
    except UserNotParticipant:
        return False
    except Exception as e:
        LOGGER.error(f"{e} for {chat.id}")
        return False


async def is_paid(user_id):
    if chat := await get_chat_info(Config.PAID_CHANNEL_ID):
        return await check_is_paid(chat, user_id)
    return True


async def token_check(user_id, button=None):
    token_timeout = Config.TOKEN_TIMEOUT
    if not token_timeout or user_id == Config.OWNER_ID:
        return None, button
    if Config.PAID_CHANNEL_ID and await is_paid(user_id):
        return None, button

    user_data.setdefault(user_id, {})
    data = user_data[user_id]
    data["TIME"] = await database.get_token_expiry(user_id)
    expire = data.get("TIME")
    isExpired = expire is None or (time() - expire) > token_timeout
    if isExpired:
        token = data["TOKEN"] if expire is None and "TOKEN" in data else str(uuid4())
        if expire is not None:
            del data["TIME"]
        data["TOKEN"] = token
        await database.update_user_token(user_id, token)
        user_data[user_id] = data

        time_str = get_readable_time(token_timeout, True)
        button = button or ButtonMaker()
        short_link = await short(
            f"https://telegram.me/{TgClient.NAME}?start={token}",
        )
        button.url_button("Collect token", short_link)
        msg = "Your token has expired, please collect a new token"
        if Config.PAID_CHANNEL_ID and Config.PAID_CHANNEL_LINK:
            msg += " or subscribe to the paid channel for no token."
            button.url_button("Subscribe", Config.PAID_CHANNEL_LINK)

        return (msg + f"\n<b>It will expire after {time_str}</b>!"), button

    return None, button
