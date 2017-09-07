from telegram import ReplyKeyboardMarkup, KeyboardButton

import strings
import bsoup

def start(bot, update):
    button = KeyboardButton(f"Send your location {strings.WORLD}",
        request_location=True)
    keyboard = ReplyKeyboardMarkup([[button]], resize_keyboard=True, 
        one_time_keyboard=True)
    update.message.reply_text(strings.GREETING_TEXT, reply_markup=keyboard)

def location(bot, update):
    location = update.message.location
    lat = location.latitude
    lon = location.longitude
    bsoup.soup(bot, update, lat, lon)

def iridium(bot, update):
    update.message.reply_text(strings.IRIDIUM_STRING)

def get_help(bot, update):
    update.message.reply_text(strings.HELP_STRING)
