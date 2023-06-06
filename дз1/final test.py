import telebot
import random

bot = telebot.TeleBot('5658799320:AAF3mW679oUwCWopzc25tjxHzZgYbK2rYLs')

jokes = ["Почему утка летит на юг зимой? Потому что это слишком далеко, чтобы идти пешком.",
         "Почему у рыбы нет денег? Потому что она всегда банкрот.",
         "Почему у кита так много друзей? Потому что он всегда в центре внимания."]

@bot.message_handler(commands=['start', 'help'])
def send_welcome(message):
    bot.reply_to(message, "Привет! Я твой новый телеграм бот. Список доступных команд:\n/start - начать работу с ботом\n/help - список доступных команд\n/joke - случайная шутка\n/sticker - отправить стикер\n/mysticker - отправить свой стикер")

@bot.message_handler(commands=['joke'])
def send_joke(message):
    bot.reply_to(message, random.choice(jokes))

@bot.message_handler(commands=['sticker'])
def send_sticker(message):
    bot.send_sticker(message.chat.id, 'CAADAgADZgkAAnlc4gmfCor5YbYYRAI')

@bot.message_handler(commands=['mysticker'])
def send_my_sticker(message):
    bot.send_sticker(message.chat.id, 'sticker')

@bot.message_handler(func=lambda message: True)
def echo_all(message):
    bot.reply_to(message, message.text)

bot.polling()