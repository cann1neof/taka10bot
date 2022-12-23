from settings import token

from telegram.ext import ApplicationBuilder, CommandHandler

from handlers.handler_hello import hello
from handlers.handler_register import register
from handlers.handler_seewho import get_pair
from handlers.handler_generation import gen_targets

def application():
    app = ApplicationBuilder().token(token).build()
    app.add_handler(CommandHandler("start", hello))
    app.add_handler(CommandHandler("register", register))
    app.add_handler(CommandHandler("gen_targets", gen_targets))
    app.add_handler(CommandHandler('seeWho', get_pair))
    app.run_polling()