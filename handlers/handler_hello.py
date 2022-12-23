from telegram import Update
from telegram.ext import ContextTypes

async def hello(update: Update, context: ContextTypes):
    await update.message.reply_text(f'Hello, {update.effective_user.first_name}!')