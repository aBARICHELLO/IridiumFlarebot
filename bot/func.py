from telegram import ReplyKeyboardMarkup, KeyboardButton

import strings

def start(bot, update):
    update.message.reply_text("Send me your location")

def get_help(bot, update):
    update.message.reply_text(strings.HELP_STRING)

def iridium(bot, update):
    update.message.reply_text(strings.IRIDIUM_STRING)