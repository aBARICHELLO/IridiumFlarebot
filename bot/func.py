from telegram import ReplyKeyboardMarkup, KeyboardButton, ParseMode

import strings
import bsoup

def start(bot, update):
    button = KeyboardButton(f"Send your location {strings.WORLD}",
        request_location=True)
    keyboard = ReplyKeyboardMarkup([[button]], resize_keyboard=True, 
        one_time_keyboard=True)
    update.message.reply_text(strings.TELESCOPE + strings.GREETING_TEXT, reply_markup=keyboard)

def location(bot, update):
    location = update.message.location
    lat = location.latitude
    lon = location.longitude
    bsoup.soup(bot, update, lat, lon)

def iridium(bot, update):
    update.message.reply_text(strings.IRIDIUM_STRING + strings.SATELLITE)
    bot.send_photo(chat_id=update.message.chat_id, photo='http://i.imgur.com/rg4WqZN.jpg')
    update.message.reply_text(strings.IRIDIUM_STRING2)
    bot.send_photo(chat_id=update.message.chat_id, photo='http://i.imgur.com/D33NXxV.jpg')

def what(bot, update):
    bot.send_message(chat_id=update.message.chat_id, 
    text=strings.WHAT_STRING,
    parse_mode=ParseMode.MARKDOWN)

def get_help(bot, update):
    update.message.reply_text(strings.HELP_STRING)
    update.message.reply_text(strings.CONTRIBUTE_STRING)
