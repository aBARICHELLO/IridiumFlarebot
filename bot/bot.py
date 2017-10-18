import logging
from telegram.ext import Updater, CommandHandler, MessageHandler
from telegram.ext import Filters, Job

import func
import config

logging.basicConfig(format='%(asctime)s - %(name)s - %(levelname)s - %(message)s',
    level=logging.DEBUG)
logger = logging.getLogger(__name__)

def error_callback(bot, update, error):
    logging.error(error)

updater = Updater(token=config.BOT_TOKEN)
dp = updater.dispatcher
job = updater.job_queue

dp.add_error_handler(error_callback)
dp.add_handler(CommandHandler('start', func.start))
dp.add_handler(CommandHandler('iridium', func.iridium))
dp.add_handler(CommandHandler('remindme', func.remindme,
    pass_args=True, pass_job_queue=True, pass_chat_data=True))
dp.add_handler(CommandHandler('unremindme', func.unremindme,
    pass_chat_data=True))
#dp.add_handler(CommandHandler('next', func.remindnext))
dp.add_handler(CommandHandler('what', func.what))
dp.add_handler(CommandHandler('help', func.get_help))
dp.add_handler(MessageHandler(Filters.location, func.location))

updater.start_webhook(listen='0.0.0.0', port=config.PORT, url_path=config.BOT_TOKEN)
updater.bot.setWebhook("https://" + config.APPNAME + ".herokuapp.com/" + config.BOT_TOKEN)
updater.idle()
