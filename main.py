import telebot
from telebot import types

# Створи бота із використанням токену
bot = telebot.TeleBot('7612829192:AAEAG9bQprJbpGG7HI0kN1psxR__e3LM5UY')


# Функція, яка обробляє команду /start
@bot.message_handler(commands=['start'])
def start(message):
    markup = types.InlineKeyboardMarkup()

    # Кнопка, яка відкриває веб-додаток (встав своє посилання)
    button = types.InlineKeyboardButton("Перейти до веб додатку",
                                        url="http://127.0.0.1:8000/employee/telegram/{}".format(message.from_user.id))
    markup.add(button)

    bot.send_message(message.chat.id, "Статистика заробітньої плати", reply_markup=markup)


# Запуск бота
bot.polling()
