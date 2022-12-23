import json

from pprint import pprint

from telegram import Update
from telegram.ext import ContextTypes

async def register(update: Update, context: ContextTypes):
    try:
        f = open('users.json', 'r')
    except FileExistsError():
        await update.message.reply_text(f'Sorry, error occured in server! Try again later!')
        return
    
    users_raw = f.read()
    pprint(users_raw)
    f.close()

    users = json.loads(users_raw)
    
    user = update.effective_user.to_dict()

    if user not in users:
        users.append(user)
        print(users)
        try:
            f = open('users.json', 'w')
        except FileExistsError():
            await update.message.reply_text(f'Sorry, error occured in server! Try again later!')
            return
        f.write(json.dumps(users))
        f.close()
        await update.message.reply_text(f'You are successfuly registered!')
        return
    
    await update.message.reply_text(f'You already registered!')