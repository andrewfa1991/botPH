import config
import telebot

bot = telebot.TeleBot(config.token)

@bot.message_handler(commands=["start"])
def first_contact(message): # Название функции не играет никакой роли
    bot.send_message(message.chat.id, "Привет. Пришли мне ссылку на свой проект на Product Hunt!")

@bot.message_handler(content_types=["text"])
def get_link(message):
    if "producthunt.com" in message.text.lower():
        bot.send_message(message.chat.id, "Вижу ссылку на Product Hunt!")
    else:
        bot.send_message(message.chat.id, "Это ссылка не на продактхант")




bot.polling(none_stop=True, interval=0)