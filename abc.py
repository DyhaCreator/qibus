import os
import telebot

bot = telebot.TeleBot('6240205037:AAFw70NAxwT5yMuGn1mMQtL0eO1i7BTvWng');
@bot.message_handler(commands=['link'])
def link(url):
    os.system('start '+url.text.split()[1])

@bot.message_handler(commands=['rickroll'])
def link(url):
    os.system('start https://www.youtube.com/watch?v=dQw4w9WgXcQ')

@bot.message_handler(content_types=['text'])
def send(message):
    print(message)

bot.polling(none_stop=True, interval=0)
