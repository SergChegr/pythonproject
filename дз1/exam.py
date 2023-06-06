import telebot

from telebot import types

bot = telebot.TeleBot("5658799320:AAF3mW679oUwCWopzc25tjxHzZgYbK2rYLs")

@bot.message_handler(commands=['start'])
def welcome(message):
    sti = open('sticker.webp', 'rb')
    bot.send_sticker(message.chat.id, sti)
    # keyboard
    markup = types.ReplyKeyboardMarkup(resize_keyboard=True)
    item1 = types.KeyboardButton("😊 Яку оцінку сьогодні отримаєш?")
    item2 = types.KeyboardButton("😃 Як справи?")

    markup.add(item1, item2)


    bot.send_message(message.chat.id, f"Вітаю, {message.from_user.first_name}!".format(message.from_user, bot.get_me()),parse_mode='html', reply_markup=markup)

@bot.message_handler(commands=['joke'])
def welcome(message):
    bot.send_message(message.chat.id, "Люди заводять дітей, тому що бояться, що в старості не розберуться з новими технологіями.")

@bot.message_handler(commands=['sticker'])
def send_welcome(message):
    stiq = open('sticker2.webp', 'rb')
    bot.send_sticker(message.chat.id, stiq)

@bot.message_handler(content_types=['text'])
def lalala(message):
    if message.text.lower() == "що робиш?":
        bot.send_mesaage(message.chat.id, 'Роблю домашку, а ти?   ')

bot.polling()



