import json

from telegram import Update
from telegram.ext import ContextTypes

async def get_pair(update: Update, context: ContextTypes):
    f = open('pairs.json', 'r')
    pairs = json.loads(f.read())
    f.close()

    for each in pairs:
        if each['user'] == update.effective_user.username:
            print(f'Your target in Secret Santa is @{each["target"]}')
            await update.message.reply_text(f'Your target in Secret Santa is @{each["target"]}')
            return
    await update.message.reply_text("You don't have a pair yet :( Register now and wait for new pairing!")
