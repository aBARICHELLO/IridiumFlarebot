from datetime import datetime
from dateutil.parser import parse
from telegram import ReplyKeyboardMarkup, KeyboardButton, ParseMode

import strings
import bsoup
import config

def start(bot, update):
    button = KeyboardButton("Send your location {}".format(strings.WORLD),
        request_location=True)
    keyboard = ReplyKeyboardMarkup([[button]], resize_keyboard=True,
        one_time_keyboard=True)
    update.message.reply_text(strings.TELESCOPE + strings.GREETING_TEXT, reply_markup=keyboard)

def location(bot, update):
    location = update.message.location
    lat = location.latitude
    lon = location.longitude
    bsoup.soup(bot, update, lat, lon)

def reminder(bot, job): # Reminder message
    bot.send_message(job.context, text=strings.REMIND_MSG)

def forward(bot, update, job_queue, chat_data): # Receive the timestamp and set reminder
    chat_id = update.message.chat_id
    contents = update.message.text

    today = datetime.now()
    try:
        contents = "".join(contents)
        contents = parse(contents)
        
        delta = (contents - today).total_seconds()
        delta = int(delta - config.SECONDS_BEFORE)
        
        if delta < 0 or delta > config.SECONDS_MAX:
            update.message.reply_text(strings.INVALID_DATE)
            return

        job = job_queue.run_once(reminder, delta, context=chat_id)
        chat_data['job'] = job
        update.message.reply_text(strings.SUCESSFULL_TIME)
    except (IndexError, ValueError):
        update.message.reply_text(strings.REMIND_HELP)

def unremindme(bot, update, chat_data): # Remove reminders
    if 'job' not in chat_data:
        update.message.reply_text(strings.NO_TIMER)
        return

    job = chat_data['job']
    job.schedule_removal()
    del chat_data['job']

    update.message.reply_text(strings.REMINDER_DELETE)

def get_help(bot, update):
    update.message.reply_text(strings.HELP_STRING)

def iridium(bot, update): # Iridium explanation
    update.message.reply_text(strings.IRIDIUM_STRING + strings.ANTENNA)
    bot.send_photo(chat_id=update.message.chat_id, photo='http://i.imgur.com/rg4WqZN.jpg')
    update.message.reply_text(strings.IRIDIUM_STRING2)
    bot.send_photo(chat_id=update.message.chat_id, photo='http://i.imgur.com/D33NXxV.jpg')

def what(bot, update): # Glossary
    bot.send_message(chat_id=update.message.chat_id,
        text=strings.WHAT_STRING,
        parse_mode=ParseMode.MARKDOWN)

def remindme(bot, update): # Explains how to use the remind system
    update.message.reply_text(strings.REMIND_HELP)
