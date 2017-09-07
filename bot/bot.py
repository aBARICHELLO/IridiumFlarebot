import logging
from telegram.ext import Updater, CommandHandler, MessageHandler, Filters

import func
import config

logging.basicConfig(format='%(asctime)s - %(name)s - %(levelname)s - %(message)s',
    level=logging.DEBUG)
logger = logging.getLogger(__name__)

def error_callback(bot, update, error):
    logging.error(error)

updater = Updater(token=config.BOT_TOKEN)
dp = updater.dispatcher
dp.add_error_handler(error_callback)
dp.add_handler(CommandHandler('start', func.start))
dp.add_handler(CommandHandler('iridium', func.iridium))
dp.add_handler(CommandHandler('help', func.get_help))
dp.add_handler(MessageHandler(Filters.location, func.location))

updater.start_polling()
updater.idle()
