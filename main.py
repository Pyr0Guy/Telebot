import os 
import telebot as tb
from telebot import types
from choice import adminButton, employeeButton, adminAuth

#Токен
with open(".env", "r") as f:
    token = f.read()

bot = tb.TeleBot(token)

#При вводе команды старт отображать кнопки
@bot.message_handler(commands=["start"])
def start(message):
	#Сами кнопки
	buttonLogin = types.ReplyKeyboardMarkup()
	buttonLogin.add(types.KeyboardButton('Начать как сотрудник'), types.KeyboardButton('Начать как администратор'))

	msg = bot.send_message(message.chat.id, 'Выберете пользователя', reply_markup=buttonLogin)

	bot.register_next_step_handler(msg, user_answer)


def user_answer(message):
	if(message.text == "Начать как администратор"):
		msg = bot.send_message(message.chat.id, adminButton())
		bot.register_next_step_handler(msg, admin_reg)
	elif(message.text == "Начать как сотрудник"):
		msg = bot.send_message(message.chat.id, employeeButton())
		bot.register_next_step_handler(msg, user_reg)
	else:
		msg = bot.send_message(message.chat.id, "Неправильно")
		bot.register_next_step_handler(msg, start)


def admin_reg(message):
	try:
		password = message.text

		if adminAuth(password) == "Пароль не правильный":
			msg = bot.send_message(message.chat.id, adminAuth(password))
			bot.register_next_step_handler(msg, admin_tools)
		elif adminAuth(password) == "Добро пожаловать":
			msg = bot.send_message(message.chat.id, adminAuth(password))
			bot.register_next_step_handler(msg, admin_tools)

	except Exception as e:
		bot.reply_to(message, 'Не сработало')

def user_reg(message):
	try:

	except Exception as e:
		bot.reply_to(message, 'Не сработало')	

bot.enable_save_next_step_handlers(delay=2)
bot.load_next_step_handlers()
#Врубаем бота
bot.infinity_polling()