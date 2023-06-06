import telebot
import random

bot = telebot.TeleBot('5658799320:AAF3mW679oUwCWopzc25tjxHzZgYbK2rYLs')

jokes = ["Почему математики плохие в приготовлении пищи? Они всегда путают таблетки с ложками.",
 "Почему у программистов всегда холодные руки? Они постоянно работают с ледяными кубиками.",
 "Почему у физиков никогда не бывает времени? Они всегда заняты изучением пространства."]

dialogue = {"Привет": "Привет! Как дела?",
 "Хорошо": "Отлично! Что нового?",
 "Ничего": "Ну и ладно. Хочешь услышать шутку?",
 "Да": "Зачем волшебнику нужен компьютер? Чтобы проверить свою почту.",
 "Нет": "Окей, может быть в другой раз.",
 "Пока": "Пока! До скорой встречи.",
 "Как дела?": "У меня все хорошо, спасибо. А у тебя?",
 "Что делаешь?": "Я отвечаю на сообщения пользователей. А ты?",
 "Сколько времени?": "Извини, я не могу сказать точное время. У меня нет доступа к часам.",
 "Кто ты?": "Я телеграм-бот, созданный для общения с пользователями."}

@bot.message_handler(commands=['start'])
def send_welcome(message):
 bot.reply_to(message, "Привет! Я твой новый телеграм-бот.")

@bot.message_handler(commands=['help'])
def send_help(message):
 bot.reply_to(message, "Доступные команды:\n/start - приветственное сообщение\n/help - список доступных команд\n/joke - случайная шутка\n/audio - отправить аудио файл\n/sticker - отправить стикер")

@bot.message_handler(commands=['joke'])
def send_joke(message):
 bot.reply_to(message, random.choice(jokes))

@bot.message_handler(commands=['audio'])
def send_audio(message):
    audio = open('audiofile.mp3', 'rb')
    bot.send_audio(message.chat.id, audio)

@bot.message_handler(commands=['sticker'])
def send_sticker(message):
    sticker = open('sticker.webp', 'rb')
    bot.send_sticker(message.chat.id, sticker)

@bot.message_handler(func=lambda message: True)
def echo_all(message):
 if message.text in dialogue:
    bot.reply_to(message, dialogue[message.text])
 else:
    bot.reply_to(message, message.text)

bot.polling()