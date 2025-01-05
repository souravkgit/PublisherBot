from functools import wraps
from MainBot import ADMINS, OWNER_ID
from telegram import Update
from telegram.ext import ContextTypes
from MainBot.modules.helper_funcs.helper import reply_to_message


def owner_command(func):
    global OWNER_ID

    @wraps(func)
    async def is_owner(
        update: Update, context: ContextTypes.DEFAULT_TYPE, *args, **kwargs
    ):
        user = update.effective_user
        query = update.callback_query
        user_id = str(user.id)
        if query:
            user_id = str(query.from_user.id)
            if user_id == OWNER_ID:
                await query.answer("You can't use this.")
            else:
                await func(update, context, *args, **kwargs)
            return
        message = update.effective_message
        if user_id == OWNER_ID:
            return await func(update, context, *args, **kwargs)
        else:
            await reply_to_message(
                message,
                "You are not allowed to use this.",
                context.bot,
                update.effective_chat.id,
            )

    return is_owner


def group_command(func):
    @wraps(func)
    async def is_command_used_in_group(
        update: Update, context: ContextTypes.DEFAULT_TYPE, *args, **kwargs
    ):
        query = update.callback_query
        if query:
            chat = query.message.chat
            if chat.type == "private":
                await query.answer("Please use this in groups only.")
            else:
                await func(update, context, *args, **kwargs)
            return
        chat = update.effective_chat
        message = update.effective_message
        if chat.type == "private":
            return await reply_to_message(
                message,
                "Please use the command in groups only.",
                context.bot,
                update.effective_chat.id,
            )
        else:
            return await func(update, context, *args, **kwargs)

    return is_command_used_in_group


def dm_command(func):
    @wraps(func)
    async def is_command_used_in_group(
        update: Update, context: ContextTypes.DEFAULT_TYPE, *args, **kwargs
    ):
        query = update.callback_query
        if query:
            chat = query.message.chat
            if chat.type != "private":
                await query.answer("Please use this in dm only.")
            else:
                await func(update, context, *args, **kwargs)
            return
        chat = update.effective_chat
        message = update.effective_message
        if chat.type != "private":
            return await reply_to_message(
                message,
                "Please use this in dm only.",
                context.bot,
                update.effective_chat.id,
            )
        else:
            return await func(update, context, *args, **kwargs)

    return is_command_used_in_group


def admin_command(func):
    global ADMINS

    @wraps(func)
    async def is_admin(
        update: Update, context: ContextTypes.DEFAULT_TYPE, *args, **kwargs
    ):
        user = update.effective_user
        query = update.callback_query
        user_id = str(user.id)
        if query:
            user_id = str(query.from_user.id)
            if user_id not in ADMINS:
                await query.answer("You can't use this.")
            else:
                await func(update, context, *args, **kwargs)
            return
        message = update.effective_message
        if user_id in ADMINS:
            return await func(update, context, *args, **kwargs)
        else:
            await reply_to_message(
                message,
                "You are not allowed to use this.",
                context.bot,
                update.effective_chat.id,
            )

    return is_admin
