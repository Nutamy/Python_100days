import telebot
import os
import re

TOKEN = os.environ["TOKEN"]
bot = telebot.TeleBot(TOKEN)

# @bot.message_handler(commands=['start', 'help'])
# def send_welcome(message):
# 	bot.reply_to(message, "Howdy, how are you doing?")


@bot.message_handler(commands=['start'])
def start(message):
  sent = bot.send_message(message.chat.id, 'Please enter the date you wish to travel in.')
  bot.register_next_step_handler(sent, hello)


def hello(message):
    flag = True
    while flag:
        date = message.text
        pattern_date = r"\d\d\d\d-\d\d-\d\d"
        match = re.fullmatch(pattern_date, date)
        if match is not None:
            bot.send_message(message.chat.id, 'The date which you have chosen ' + date)
            bot.send_message(message.chat.id, 'Bon Voyage and get there safe!')
            flag = False
        else:
            bot.send_message(message.chat.id, 'Please enter the date in format YYYY-MM-DD')
            date = message.text

bot.infinity_polling()