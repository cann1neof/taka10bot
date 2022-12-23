import json
import requests

from random import choice

from telegram import Update
from telegram.ext import ContextTypes

from WrongUserException import WrongUserException

from settings import token

def choose_user(choosen, user, users):
    try:
        target = choice(users)
        if target in choosen or target == user:
            raise WrongUserException
    except WrongUserException:
        return choose_user(choosen, user, users)
    return target

def send_hi(choosen):
    for each in choosen: 
        url = f"https://api.telegram.org/bot{token}/sendMessage?chat_id={each['id']}&text={'We found you a pair! Type /seeWho to see who is it!'}"
        print(requests.get(url).json())

async def gen_targets(update: Update, context: ContextTypes):
    if update.effective_user.username != 'cann1neof':
        return
    
    f = open('users.json', 'r')
    users = json.loads(f.read())
    f.close()

    pairs = []
    choosen = []
    for user in users:
        target = choose_user(choosen, user, users)
        
        pairs.append({'user': user['username'], 'target': target['username']})
        choosen.append(target)

        print('pairs', pairs)
    
    if len(pairs) == len(users):
        f = open('pairs.json', 'w')
        f.write(json.dumps(pairs))
        f.close()
    await update.message.reply_text(json.dumps(pairs))
    
    send_hi(choosen)
