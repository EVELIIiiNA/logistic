from baza import *
import telebot
from telebot import types

bot = telebot.TeleBot("2014583654:AAG_T0hQKe0JHPHmSGeayFFB6dmTdM43p6I")
keybord1=types.ReplyKeyboardMarkup(True, row_width=2)
car=types.KeyboardButton("Найти транспорт")
cargo=types.KeyboardButton("Найти груз")
keybord1.add(car, cargo)

data ={"car":"Найти транспорт",
       "cargo": "Найти груз"}

# name='';
# jurname='';
# ynp = "";
# directionfrom = '';
# direectionat= '';
# weight='';

@bot.message_handler(commands=['start'])
def start_message(message):
    bot.send_message(message.chat.id,"Чем помочь?",reply_markup=keybord1)


@bot.message_handler(content_types=['text'])
def text(message):
    if message.text in data.keys():
        bot.send_message(message.chat.id, 'Ок! Как к Вам обращаться?')
        bot.register_next_step_handler(message, get_name)
    print(message.text)

def get_name(message):
    global name
    name = message.text
    bot.send_message(message.from_user.id, 'Ведите название предприятия/ип?')
    bot.register_next_step_handler(message, get_jurname)

def get_jurname(message):
    global jurname
    jurname = message.text
    bot.send_message(message.from_user.id, 'Укажитне Ваш унп')
    bot.register_next_step_handler(message, get_unp)

def get_unp(message):
    global unp
    unp = message.text
    if keybord1== "Найти транспорт":
        bot.send_message(message.from_user.id, 'Откуда забрать груз?')
    else:
        bot.send_message(message.from_user.id, 'Где находится Ваш транспорт?')
    bot.register_next_step_handler(message, get_unp)

bot.polling()
