from telegram.constants import ParseMode


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
