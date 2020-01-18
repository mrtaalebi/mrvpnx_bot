import os

import telegram
from telegram.ext import Updater


bot_token = os.getenv('BOT_TOKEN')
if bot_token is None:
    raise Exception('BOT_TOKEN env has not been set. exiting.')

updater = Updater(token=bot_token)
dispatcher = updater.dispatcher

import logging
logging.basicConfig(
        format='%(asctime)s - %(name)s - %(levelname)s - %(message)s',
        level=logging.INFO
)

def start(update, context):
    context.bot.send_message(chat_id=update.effective_chat.id, text="I'm a bot, please talk to me!")

