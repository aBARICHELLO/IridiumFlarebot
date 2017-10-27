from datetime import datetime
from dateutil.parser import parse
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

def iridium(bot, update): # Iridium explanation
    update.message.reply_text(strings.IRIDIUM_STRING + strings.ANTENNA)
    bot.send_photo(chat_id=update.message.chat_id, photo='http://i.imgur.com/rg4WqZN.jpg')
    update.message.reply_text(strings.IRIDIUM_STRING2)
    bot.send_photo(chat_id=update.message.chat_id, photo='http://i.imgur.com/D33NXxV.jpg')

def what(bot, update): # Glossary
    bot.send_message(chat_id=update.message.chat_id,
        text=strings.WHAT_STRING,
        parse_mode=ParseMode.MARKDOWN)

def reminder(bot, job): # Reminder message
    bot.send_message(job.context, text=strings.REMIND_MSG)

def remindme(bot, update, args, job_queue, chat_data): # Remind setter
    chat_id = update.message.chat_id

    today = datetime.now()
    try:
        args = "".join(args)

        args = parse(args)
        delta = (args - today).total_seconds()
        print(args)
        print(today)
        print(delta)

        delta = int(delta-strings.SECONDS_BEFORE)
        if delta < 0 or delta > strings.SECONDS_MAX:
            update.message.reply_text('Invalid date!')
            return
        job = job_queue.run_once(reminder, delta, context=chat_id)
        chat_data['job'] = job
        update.message.reply_text(strings.SUCESSFULL_TIME)
    except (IndexError, ValueError):
        update.message.reply_text(strings.USAGE_ERROR)

def unremindme(bot, update, chat_data):
    if 'job' not in chat_data:
        update.message.reply_text('You don\'t have a timer set!')
        return

    job = chat_data['job']
    job.schedule_removal()
    del chat_data['job']

    update.message.reply_text('You will no longer be reminded!')

def get_help(bot, update):
    update.message.reply_text(strings.HELP_STRING)
