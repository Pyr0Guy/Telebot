import os 
import telebot as tb
from telebot import types
from choice import adminButton, employeeButton, adminAuth
from base import registerUser, showUsers
from admin import addUser

#Токен
with open(".env", "r") as f:
    token = f.read()

bot = tb.TeleBot(token)

inAdmin = False

#При вводе команды старт отображать кнопки
@bot.message_handler(commands=["start"])
def start(message):
	#Сами кнопки
	buttonLogin = types.ReplyKeyboardMarkup()
	buttonLogin.add(types.KeyboardButton('Начать как сотрудник'), types.KeyboardButton('Начать как администратор'))

	msg = bot.send_message(message.chat.id, 'Выберете пользователя', reply_markup=buttonLogin)

	bot.register_next_step_handler(msg, user_answer)

#Получаем ответ от чувачка
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

#Вводим крутой пароль
def admin_reg(message):
	try:
		password = message.text

		if adminAuth(password) == "Пароль не правильный":
			msg = bot.send_message(message.chat.id, adminAuth(password))
			bot.register_next_step_handler(msg, start)
		elif adminAuth(password) == "Добро пожаловать":
			msg = bot.send_message(message.chat.id, adminAuth(password))
			bot.register_next_step_handler(msg, admin_tools)

	except Exception as e:
		bot.reply_to(message, 'Не сработало')

#Иструменты админа
def admin_tools(message):
	buttonAdmin = types.ReplyKeyboardMarkup()
	buttonAdmin.add(types.KeyboardButton('Добавить сотрудника'), types.KeyboardButton('Проверить сотрудников'), types.KeyboardButton('Выход'))

	msg = bot.send_message(message.chat.id, "Добро пожаловать", reply_markup=buttonAdmin)
	bot.register_next_step_handler(msg, admin_answer)

def admin_answer(message):
	if(message.text == "Добавить сотрудника"):
		msg = bot.send_message(message.chat.id, "Введите имя")
		bot.register_next_step_handler(msg, admin_addUser)
	elif(message.text == "Проверить сотрудников"):
		msg = bot.send_message(message.chat.id, "Вот")
		bot.register_next_step_handler(msg, admin_showUsers)
	else:
		msg = bot.send_message(message.chat.id, "Пока")
		bot.register_next_step_handler(msg, start)

def admin_addUser(message):
	name = message.text
	addUser(name, "employee")
	msg = bot.reply_to(message, 'Complete')
	bot.register_next_step_handler(msg, admin_tools)

def admin_showUsers(message):
	users = [showUsers()]
	print(users)
	for i in range(len(showUsers())):
		msg = bot.send_message(message.chat.id, users[0][i])

	bot.register_next_step_handler(msg, admin_tools)

def user_reg(message):
	try:
		print("lol")
	except Exception as e:
		bot.reply_to(message, 'Не сработало')	

bot.enable_save_next_step_handlers(delay=2)
bot.load_next_step_handlers()
#Врубаем бота
bot.infinity_polling()