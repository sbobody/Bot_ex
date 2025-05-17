import telebot # библиотека telebot
from config import token # импорт токена
import logic

bot = telebot.TeleBot(token) 

@bot.message_handler(commands=['start'])
def start(message):
    bot.reply_to(message, "Привет! Я бот для подготовки к экзаменам.")



@bot.message_handler(content_types=['text'])
def echo_message(message):

    bot.reply_to(message, logic.gpt (message.text)) 

bot.infinity_polling(none_stop=True)