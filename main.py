import os 
import telebot as tb
from telebot import types
from choice import adminButton, employeeButton, adminAuth
from base import registerUser, showUsers, vabalabda, showUsersNAME, addDescription
from user import userComp, userWork1, userWork2
from admin import addUser, companyInfo, userText1, userText2, userText3

#Токен

bot = tb.TeleBot("5973367934:AAH5QSC-UkZDrueAg3p0a9OoowuONWcaUko")


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

			buttonAdmin = types.ReplyKeyboardMarkup()
			buttonAdmin.add(types.KeyboardButton('Добавить сотрудника'), types.KeyboardButton('Проверить сотрудников'), types.KeyboardButton('Выход'))

			msg = bot.send_message(message.chat.id, "Добро пожаловать", reply_markup=buttonAdmin)
			bot.register_next_step_handler(msg, admin_answer)

	except Exception as e:
		bot.reply_to(message, 'Не сработало')

#Иструменты админа
#def admin_tools(message):
#	buttonAdmin = types.ReplyKeyboardMarkup()
#	buttonAdmin.add(types.KeyboardButton('Добавить сотрудника'), types.KeyboardButton('Проверить сотрудников'), types.KeyboardButton('Выход'))
#
#	msg = bot.send_message(message.chat.id, "Добро пожаловать", reply_markup=buttonAdmin)
#	bot.register_next_step_handler(msg, admin_answer)

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
	sus = addUser(name, "employee")
	msg = bot.reply_to(message, sus)
	start(message)
	#bot.register_next_step_handler(msg, admin_tools)

def admin_showUsers(message):
	users = showUsers()
	print(users)
	for i in range(len(showUsers())):
		for j in range(3):
				msg = bot.send_message(message.chat.id, users[i][j])

	start(message)
#	bot.register_next_step_handler(msg, admin_reg)

#Инструменты пользователя
def user_reg(message):
	#try:
	#msg = bot.send_message(message.chat.id, "Введите персональный код: ")
	print(vabalabda(message.text))
	a = message.text
	if vabalabda(a) == [(1,)]: 
		msg = bot.send_message(message.chat.id, "Доступ получен")
		buttonUser = types.ReplyKeyboardMarkup()
		buttonUser.add(types.KeyboardButton('Обучение профессии'), types.KeyboardButton('Посмотреть коллег'), types.KeyboardButton('О компании'), types.KeyboardButton('Настройки'), types.KeyboardButton('Выход')) 

		msg = bot.send_message(message.chat.id, "Выберете кнопку", reply_markup=buttonUser)
		bot.register_next_step_handler(msg, user_answer2)
	else:
		bot.send_message(message.chat.id, "Неверный персональный код ")
		start(message)
	

	#except Exception as e:
	#	bot.reply_to(message, 'Не сработало')

#def user_tools(message): 
	#buttonUser = types.ReplyKeyboardMarkup()
	#buttonUser.add(types.KeyboardButton('Обучение профессии'), types.KeyboardButton('Посмотреть коллег'), types.KeyboardButton('О компании'), types.KeyboardButton('Настройки'), types.KeyboardButton('Выход')) 
	#buttonUser.add(types.KeyboardButton('О компании'), types.KeyboardButton('Выход')) 
	#msg = bot.send_message(message.chat.id, "Выберите, что хотите сделать: ", reply_markup=buttonUser)
	#bot.register_next_step_handler(msg, user_answer2)

def user_answer2(message):
	if(message.text == "Обучение профессии"):
		print("Обучение профессии")
		msg = bot.send_message(message.chat.id, "Вот информация по вашей профессии:")
		bot.register_next_step_handler(msg, user_GuideBook)
	elif(message.text == "Посмотреть коллег"):
		print("Проверка сотрудников")
		msg = bot.send_message(message.chat.id, "Вот информация о ваших коллегах:")
		bot.register_next_step_handler(msg, user_showUsers)
	elif(message.text == "О компании"):
		msg = bot.send_message(message.chat.id, "Вот информация о нашей компании:")
		bot.register_next_step_handler(msg, user_showСompan)
	elif(message.text == "Настройки"):
		buttonsettings = types.ReplyKeyboardMarkup()
		buttonsettings.add(types.KeyboardButton('Изменить информацию о себе'), types.KeyboardButton('Выход'))
		msg = bot.send_message(message.chat.id, "Вот возможные настройки: ", reply_markup=buttonsettings)
		bot.register_next_step_handler(msg, settings)
	else:
		msg = bot.send_message(message.chat.id, "bb")
		bot.register_next_step_handler(msg, start)

def settings(message):
	if(message.text == "Изменить информацию о себе"):
		msg = bot.send_message(message.chat.id, "Введите персональный код для подтверждения: ")
		bot.register_next_step_handler(msg, settings3)
	elif(message.text == "Выход"):
		bot.register_next_step_handler(msg, user_answer2)

def settings2(message):
	global a
	a = message.text
	if (vabalabda(a) == [(1,)]): 
		msg = bot.send_message(message.chat.id, "Доступ получен")
		name = message.text
		addDescription(name, a)
		print(addDescription(name, a))
		bot.register_next_step_handler(msg, settings)
	else:
		bot.send_message(message.chat.id, "Неверный персональный код ")
		bot.register_next_step_handler(msg, settings)

def user_GuideBook(message):
	msg = bot.send_message(message.chat.id, userWork1())
	bot.register_next_step_handler(msg, user_GuideBook2)

def user_GuideBook2(message):
	msg = bot.send_message(message.chat.id, userWork2())
	bot.register_next_step_handler(msg, user_reg)

def user_GuideBook3(message):
	msg = bot.send_message(message.chat.id, userText3())
	bot.register_next_step_handler(msg, start)

def user_showUsers(message):
	users = showUsers()
	print(users)
	for i in range(len(showUsers())):
		msg = bot.send_message(message.chat.id, users[i])

	bot.register_next_step_handler(msg, user_question)

def user_showСompan(message):
	msg = bot.send_message(message.chat.id, userComp())
	bot.register_next_step_handler(msg, user_reg)
	msg = bot.send_message(message.chat.id, companyInfo())
	bot.register_next_step_handler(msg, start)

def user_question(message):
	buttonUser = types.ReplyKeyboardMarkup()
	buttonUser.add(types.KeyboardButton('Подробная информация о пользователе'), types.KeyboardButton('Выход')) 
	msg = bot.send_message(message.chat.id, "Выберите, что хотите сделать дальше: ", reply_markup=buttonUser)
	bot.register_next_step_handler(msg, user_check)

def user_check(message):
	if message.text == "Подробная информация о пользователе":
		msg = bot.send_message(message.chat.id, "Введите имя пользователя о котором хотите получить информацию: ")
		bot.register_next_step_handler(msg, user_check_other_user)
	else:
		bot.register_next_step_handler(msg, user_reg)

def user_check_other_user(message):
	name = message.text
	msg = bot.send_message(message.chat.id, showUsersNAME(name))
	bot.register_next_step_handler(msg, user_reg)

bot.enable_save_next_step_handlers(delay=12)
bot.load_next_step_handlers()
#Врубаем бота
bot.polling()