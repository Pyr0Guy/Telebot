import os 
import telebot as tb
from telebot import types
from choice import adminButton, employeeButton, adminAuth
from base import registerUser, showUsers, vabalabda
from admin import addUser
from user import showGuideBook, showColleges

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
	users = showUsers()
	print(users)
	for i in range(len(showUsers())):
		for j in range(3):
				msg = bot.send_message(message.chat.id, users[i][j])

	bot.register_next_step_handler(msg, user_question)

def user_question(message):
	buttonUser = types.ReplyKeyboardMarkup()
	buttonUser.add(types.KeyboardButton('Подробная информация о пользователе'), types.KeyboardButton('Выход')) 
	msg = bot.send-message(message.chat.id, "Выберите, что хотите сделать дальше: ", reply_markup=buttonUser)
	
	if message.text == "Подробная информация о пользователе":
		msg = bot.send-message(message.chat.id, "Введите им пользователя: ")
		bot.register_next_step_handler(msg, admin_UserDescription)
	else:
		bot.register_next_step_handler(msg, admin_tools)

def admin_UserDescription(): pass
	# здесь нужно сделать вывод информации об указанном пользователе

#Инструменты пользователя
def user_reg(message):
	users = showUsers()
	try:
		msg = bot.send_message(message.chat.id, "Введите персональный код: ")
		if vabalabda(message.text) == 1: 
			msg = bot.send_message(message.chat.id, "Доступ получен")
			bot.register_next_step_handler(msg, user_tools)
		else:
			msg = bot.send_message(message.chat.id, "Неверный персональный код ")
			bot.register_next_step_handler(msg, start)

	except Exception as e:
		bot.reply_to(message, 'Не сработало')

def user_tools(message): 
	buttonUser = types.ReplyKeyboardMarkup()
	buttonUser.add(types.KeyboardButton('Обучение профессии'), types.KeyboardButton('Посмотреть коллег')) 
	buttonUser.add(types.KeyboardButton('О компании'), types.KeyboardButton('Выход')) 
	msg = bot.send-message(message.chat.id, "Выберите, что хотите сделать: ", reply_markup=buttonUser)
	bot.register_next_step_handler(msg, user_answer)

def user_answer(message): 
	if(message.text == "Обучение профессии"):
		msg = bot.send_message(message.chat.id, "Вот информация по вашей профессии: ")
		bot.register_next_step_handler(msg, user_GuideBook)
	elif(message.text == "Посмотреть коллег"):
		msg = bot.send_message(message.chat.id, "Вот информация о ваших коллегах: ")
		bot.register_next_step_handler(msg, user_showUsers)
	elif(message.text == "О компании"):
		msg = bot.send_message(message.chat.id, "Вот информация о нашей компании: ")
		bot.register_next_step_handler(msg, user_showСompany)
	else:
		msg = bot.send_message(message.chat.id, "Пока")
		bot.register_next_step_handler(msg, start)

def user_GuideBook(): pass

def user_showUsers(message):
	users = [showUsers()]
	print(users)
	for i in range(len(showUsers())):
		msg = bot.send_message(message.chat.id, users[0][i])

	bot.register_next_step_handler(msg, user_question)

def user_question(message):
	buttonUser = types.ReplyKeyboardMarkup()
	buttonUser.add(types.KeyboardButton('Подробная информация о пользователе'), types.KeyboardButton('Выход')) 
	msg = bot.send-message(message.chat.id, "Выберите, что хотите сделать дальше: ", reply_markup=buttonUser)
	
	if message.text == "Подробная информация о пользователе":
		pass
	else:
		bot.register_next_step_handler(msg, user_tools)

def user_showСompany(): pass

bot.enable_save_next_step_handlers(delay=8)
bot.load_next_step_handlers()
#Врубаем бота
bot.polling()