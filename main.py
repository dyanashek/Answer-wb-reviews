import telebot
import logging
import threading
import datetime

import config
import functions
import text
import utils

bot = telebot.TeleBot(config.TELEGRAM_TOKEN)

threading.Thread(daemon=True, target=functions.answer_unanswered).start()
threading.Thread(daemon=True, target=functions.send_daily_report).start()

@bot.message_handler(commands=['start'])
def start_message(message):
    '''Handles start command.'''

    bot.send_message(chat_id=message.chat.id,
                         text='d',
                         parse_mode='Markdown',
                         )


@bot.message_handler(commands=['status'])
def start_message(message):
    user_id = str(message.from_user.id)

    if user_id in config.MANAGER_ID:
        bot.send_message(chat_id=message.chat.id,
                         text=text.status_text(),
                         parse_mode='Markdown'
                         )
    else:
        bot.send_message(chat_id=message.chat.id,
                         text=text.PROHIBITED,
                         )


@bot.message_handler(commands=['activate'])
def start_message(message):
    user_id = str(message.from_user.id)

    if user_id in config.MANAGER_ID:
        config.ACTIVE = True
        bot.send_message(chat_id=message.chat.id,
                         text=text.ACTIVATED,
                         parse_mode='Markdown'
                         )
    else:
        bot.send_message(chat_id=message.chat.id,
                         text=text.PROHIBITED,
                         )


@bot.message_handler(commands=['deactivate'])
def start_message(message):
    user_id = str(message.from_user.id)

    if user_id in config.MANAGER_ID:
        config.ACTIVE = False
        bot.send_message(chat_id=message.chat.id,
                         text=text.DEACTIVATED,
                         parse_mode='Markdown'
                         )
    else:
        bot.send_message(chat_id=message.chat.id,
                         text=text.PROHIBITED,
                         )


@bot.message_handler(commands=['report'])
def start_message(message):
    user_id = str(message.from_user.id)

    if user_id in config.MANAGER_ID:
        current_date = message.text.replace('/report', '').replace(' ', '')
        if not current_date:
            current_date = (datetime.datetime.utcnow() + datetime.timedelta(hours=3)).strftime("%d.%m.%Y")
        else:
            if not utils.validate_date(current_date):
                current_date = None

                bot.send_message(chat_id=message.chat.id,
                         text=text.WRONG_FORMAT,
                         parse_mode='Markdown',
                         )
            
        if current_date:
            functions.send_date_report(current_date)

    else:
        bot.send_message(chat_id=message.chat.id,
                         text=text.PROHIBITED,
                         )


@bot.message_handler(commands=['report_all'])
def start_message(message):
    user_id = str(message.from_user.id)

    if user_id in config.MANAGER_ID:
        functions.send_all_report()

    else:
        bot.send_message(chat_id=message.chat.id,
                         text=text.PROHIBITED,
                         )


if __name__ == '__main__':
    # bot.polling(timeout=80)
    while True:
        try:
            bot.polling()
        except:
            pass