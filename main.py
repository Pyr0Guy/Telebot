import os 
import telebot as tb
from telebot import types
#import *


#Токен
with open(".env", "r") as f:
    token = f.read()

bot = tb.TeleBot(token)

#При вводе команды старт отображать кнопки
@bot.message_handler(commands=['start'])
def start_message(message):
	#Клавиатура для кнопок
	keyboard = types.ReplyKeyboardMarkup(row_width=2, resize_keyboard=False, one_time_keyboard=True)

	#Сами кнопки
	user  = types.KeyboardButton(text='Начать как сотрудник')
	admin = types.KeyboardButton(text='Начать как администратор')

	keyboard.add(user)
	keyboard.add(admin)

	bot.send_message(message.chat.id, 'Выберете пользователя', reply_markup=keyboard)

@bot.message_handler(commands = ["Начать как сотрудник"])
def user_start(message):
	bot.send_message(message.chat.id, 'Все мы когда-то начанали с низов, у нас было много вопросов и постоянно докучали ими всех. Чтобы больше таких казусов не случалось наша кампания создала этого телеграмм бота чтобы помочь новым сотрудникам по типу ТЕБЯ. Пройдя по ниже соответствующим кнопкам и нажав на одну из них ты узнаешь больше информации. (P.S если же ты не хочешь читать всю эту скучную информацию, если ты введешь команду «/game» тебя перенесет в особый «Игровой режим» в котором вся та же информация будет представленна ввиде маленькой визуальной новелы )', reply_markup=keyboard)

#Врубаем бота
bot.infinity_polling()