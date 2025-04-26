
import telebot
from datetime import datetime
import random

TOKEN = '7804249180:AAFnNmzCUSNAQI4EE3_ZsA_fPx1jTiDlzFc'

bot = telebot.TeleBot(TOKEN)

@bot.message_handler(commands=['start'])
def send_welcome(message):
    markup = telebot.types.ReplyKeyboardMarkup(resize_keyboard=True)
    btn1 = telebot.types.KeyboardButton('Подскажи время')
    btn2 = telebot.types.KeyboardButton('Выдай рандомное число')
    btn3 = telebot.types.KeyboardButton('Мой ID')
    markup.row(btn1, btn2, btn3)
    bot.send_message(message.chat.id, f"Привет, {message.from_user.first_name}, выбери действие:", reply_markup=markup)

@bot.message_handler(func=lambda message: True)
def handle_all_messages(message):
    if message.text == 'Подскажи время':
        current_time = datetime.now().strftime('%H:%M:%S')
        bot.send_message(message.chat.id, f"Подскажи время: {current_time}")
    elif message.text == 'Выдай рандомное число':
        rand_num = random.randint(1, 100)
        bot.send_message(message.chat.id, f"Случайное число: {rand_num}")
    elif message.text == 'Мой ID':
        bot.send_message(message.chat.id, f"Ваш ID: {message.from_user.id}")
    else:
        bot.send_message(message.chat.id, "Команда не распознана.")

bot.polling(non_stop=True)
