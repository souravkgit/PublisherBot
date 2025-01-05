from telegram.constants import ParseMode
from telegram import InlineKeyboardButton


async def reply_to_message(message, text, bot, chat_id, pm=ParseMode.MARKDOWN, rm=None):
    try:
        msgg = await message.reply_text(
            text, parse_mode=pm, reply_markup=rm, disable_web_page_preview=True
        )
        return msgg
    except Exception as e:
        print(e)
        msgg = await bot.send_message(
            chat_id, text, parse_mode=pm, reply_markup=rm, disable_web_page_preview=True
        )
        return msgg


async def send_message_to_chat(text, bot, chat_id, pm=ParseMode.MARKDOWN, rm=None):
    try:
        await bot.send_message(
            chat_id, text, parse_mode=pm, reply_markup=rm, disable_web_page_preview=True
        )
    except Exception as e:
        print(e)
        pass


async def build_keyboard(buttons):
    keyb = []
    for name, url, same_line in buttons:
        name, url
        if same_line and keyb:
            keyb[-1].append(InlineKeyboardButton(name, url=url))
        else:
            keyb.append([InlineKeyboardButton(name, url=url)])

    return keyb
