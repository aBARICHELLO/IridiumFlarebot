from telegram import ReplyKeyboardMarkup, KeyboardButton, ParseMode

from datetime import datetime
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
    update.message.reply_text(strings.IRIDIUM_STRING + strings.SATELLITE)
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
    args2 = args[2].replace(',', '')
    try:
        args = f'{args[0]} {args[1]} {args2}, {args[3]}' #format received date
    except IndexError:
        update.message.reply_text(strings.USAGE_ERROR)
    
    # transform to datetime object
    args = datetime.strptime(args, '%Y %b %d, %H:%M:%S') 
    delta = (args - today).total_seconds()
    print(args) 
    print(today)
    print(delta)
    
    try:
        delta = int(delta)
        if delta < 0:
            update.message.reply_text('Negative data!')
            return
        job = job_queue.run_once(reminder, delta, context=chat_id)
        chat_data['job'] = job
        update.message.reply_text('Time sucessfully set!')
    except (IndexError, ValueError):
        update.message.reply_text(strings.USAGE_ERROR)

def get_help(bot, update):
    update.message.reply_text(strings.HELP_STRING)
    update.message.reply_text(strings.CONTRIBUTE_STRING)
