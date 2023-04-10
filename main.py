import os 
import telebot as tb
from telebot import types
from choice import adminButton, adminAuth

#Токен
with open(".env", "r") as f:
    token = f.read()

bot = tb.TeleBot(token)

#Создаем клавиатуру с кнопками
keyboard = types.ReplyKeyboardMarkup(row_width=2, resize_keyboard=False, one_time_keyboard=True)

#При вводе команды старт отображать кнопки
@bot.message_handler(commands=['start'])
def start_message(message):

	#Сами кнопки
	user  = types.KeyboardButton(text='Начать как сотрудник')
	admin = types.KeyboardButton(text='Начать как администратор')

	keyboard.row(user, admin)
	#keyboard.add(user)
	#keyboard.add(admin)

	bot.send_message(message.chat.id, 'Выберете пользователя', reply_markup=keyboard)

#Отслеживаем каждое сообщение пользователя 
@bot.message_handler(content_types=['text'])
def echo(message):
    text = message.text
    user = message.chat.id

    if(text == "Начать как администратор"):
    	bot.register_next_step_handler(text, process_name_step)

def process_name_step(message):
	try:
		password = message.text
		bot.send_message(message,adminAuth(password), reply_markup=keyboard)
	except Exception as e:
		bot.reply_to(message, 'oooops')

#Врубаем бота
bot.infinity_polling()