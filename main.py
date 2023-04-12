import os 
import telebot as tb
from telebot import types
from choice import adminButton, employeeButton, adminAuth
from base import showUsers, vabalabda, showUsersName, showUsersGroup, addDescription, showUsersDescription, showUsersNameAdmin, showUsersIdAdmin, showUsersGroupAdmin, showUsersDescriptionAdmin
from user import userWork1, userWork2
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
		msg = bot.send_message(message.chat.id, "Такого варианта нет")
		start(message)


#Функции админа
def admin_reg(message):
	try:
		password = message.text

		if adminAuth(password) == "Пароль не правильный":
			msg = bot.send_message(message.chat.id, adminAuth(password))
			start(message)
		elif adminAuth(password) == "Добро пожаловать":
			print("Администратор вошел")
			buttonAdmin = types.ReplyKeyboardMarkup()
			buttonAdmin.add(types.KeyboardButton('Добавить сотрудника'), types.KeyboardButton('Проверить сотрудников'), types.KeyboardButton('Выход'))

			msg = bot.send_message(message.chat.id, "Добро пожаловать", reply_markup=buttonAdmin)
			bot.register_next_step_handler(msg, admin_answer)

	except Exception as e:
		bot.reply_to(message, 'Не сработало')


def admin_answer(message):
	if(message.text == "Добавить сотрудника"):
		msg = bot.send_message(message.chat.id, "Введите имя")
		bot.register_next_step_handler(msg, admin_addUser)
	elif(message.text == "Проверить сотрудников"):
		msg = bot.send_message(message.chat.id, "Вот")
		admin_showUsers(message)
	elif(message.text == "Выход"):
		start(message)
	else:
		bot.send_message(message.chat.id, "Нет такого значения")
		buttonAdmin = types.ReplyKeyboardMarkup()
		buttonAdmin.add(types.KeyboardButton('Добавить сотрудника'), types.KeyboardButton('Проверить сотрудников'), types.KeyboardButton('Выход'))

		msg = bot.send_message(message.chat.id, "Выберите, что хотите сделать дальше: ", reply_markup=buttonAdmin)
		bot.register_next_step_handler(msg, admin_answer)


def admin_addUser(message):
	name = message.text
	sus = addUser(name, "employee")
	msg = bot.reply_to(message, sus)

	buttonAdmin = types.ReplyKeyboardMarkup()
	buttonAdmin.add(types.KeyboardButton('Добавить сотрудника'), types.KeyboardButton('Проверить сотрудников'), types.KeyboardButton('Выход'))

	msg = bot.send_message(message.chat.id, "Выберите, что хотите сделать дальше: ", reply_markup=buttonAdmin)
	bot.register_next_step_handler(msg, admin_answer)


def admin_showUsers(message):
	users = showUsers()
	print(users)

	for i in range(len(showUsers())):
		bot.send_message(message.chat.id, showUsersNameAdmin(i))
		bot.send_message(message.chat.id, showUsersIdAdmin(i))
		bot.send_message(message.chat.id, showUsersGroupAdmin(i))
		bot.send_message(message.chat.id, showUsersDescriptionAdmin(i))
		bot.send_message(message.chat.id, "########################################")

	buttonAdmin = types.ReplyKeyboardMarkup()
	buttonAdmin.add(types.KeyboardButton('Добавить сотрудника'), types.KeyboardButton('Проверить сотрудников'), types.KeyboardButton('Выход'))

	msg = bot.send_message(message.chat.id, "Выберите, что хотите сделать дальше: ", reply_markup=buttonAdmin)
	bot.register_next_step_handler(msg, admin_answer)


#Функции пользователя
def user_reg(message):
	a = message.text
	if vabalabda(a) == [(1,)]: 
		print("Пользователь подключен")
		bot.send_message(message.chat.id, "Доступ получен")
		buttonUser = types.ReplyKeyboardMarkup()
		buttonUser.add(types.KeyboardButton('Обучение профессии'), types.KeyboardButton('Посмотреть коллег'), types.KeyboardButton('О компании'), types.KeyboardButton('Настройки'), types.KeyboardButton('Выход')) 
		msg = bot.send_message(message.chat.id, "Выберете кнопку", reply_markup=buttonUser)
		bot.register_next_step_handler(msg, user_answer2)
	else:
		bot.send_message(message.chat.id, "Неверный персональный код ")
		start(message)


def user_answer2(message):
	if(message.text == "Обучение профессии"):
		print("Обучение профессии")
		msg = bot.send_message(message.chat.id, "Вот информация по вашей профессии:")
		user_GuideBook(message)
	elif(message.text == "Посмотреть коллег"):
		print("Проверка сотрудников")
		msg = bot.send_message(message.chat.id, "Вот информация о ваших коллегах:")
		bot.register_next_step_handler(msg, user_showUsers)
	elif(message.text == "О компании"):
		msg = bot.send_message(message.chat.id, "Вот информация о нашей компании:")
		bot.register_next_step_handler(msg, user_showСompan)
	elif(message.text == "Настройки"):
		buttonsettings = types.ReplyKeyboardMarkup()
		buttonsettings.add(types.KeyboardButton('Изменить информацию о себе'), types.KeyboardButton('Выйти'))
		msg = bot.send_message(message.chat.id, "Вот возможные настройки: ", reply_markup=buttonsettings)
		bot.register_next_step_handler(msg, settings)
	elif(message.text == "Выход"):
		start(message)
	else:
		bot.send_message(message.chat.id, "Такого варианта нет")

		buttonUser = types.ReplyKeyboardMarkup()
		buttonUser.add(types.KeyboardButton('Обучение профессии'), types.KeyboardButton('Посмотреть коллег'), types.KeyboardButton('О компании'), types.KeyboardButton('Настройки'), types.KeyboardButton('Выход')) 
		msg = bot.send_message(message.chat.id, "Выберете кнопку", reply_markup=buttonUser)

		bot.register_next_step_handler(msg, user_answer2)


def user_GuideBook(message):
	bot.send_message(message.chat.id, userWork1())
	bot.send_message(message.chat.id, userWork2())
	msg = bot.send_message(message.chat.id, "Подтвердите выход прислав любой символ")
	bot.register_next_step_handler(msg, user_answer2)

'''
def user_GuideBook3(message):
	bot.send_message(message.chat.id, userText3())
	msg = bot.send_message(message.chat.id, "Подтвердите выход прислав любой символ")
	bot.register_next_step_handler(msg, user_answer2)
'''


def user_showUsers(message):
	users = showUsers()
	print(users)
	for i in range(len(showUsers())):
		bot.send_message(message.chat.id, users[i])

	buttonUser = types.ReplyKeyboardMarkup()
	buttonUser.add(types.KeyboardButton('Подробная информация о пользователе'), types.KeyboardButton('Выход')) 
	msg = bot.send_message(message.chat.id, "Выберите, что хотите сделать дальше: ", reply_markup=buttonUser)
	bot.register_next_step_handler(msg, user_check)

def user_check(message):
	if (message.text == "Подробная информация о пользователе"):
		usg = bot.send_message(message.chat.id, "Введите имя пользователя о котором хотите получить информацию: ")
		bot.register_next_step_handler(usg, user_check_other_user)
	elif (message.text == "Выход"):
		bot.send_message(message.chat.id, "Выберите, что хотите сделать дальше: ")

		buttonUser = types.ReplyKeyboardMarkup()
		buttonUser.add(types.KeyboardButton('Обучение профессии'), types.KeyboardButton('Посмотреть коллег'), types.KeyboardButton('О компании'), types.KeyboardButton('Настройки'), types.KeyboardButton('Выход')) 
		msg = bot.send_message(message.chat.id, "Выберете кнопку", reply_markup=buttonUser)

		bot.register_next_step_handler(msg, user_answer2)
	else:
		bot.send_message(message.chat.id, "Такого варианта нет")

		buttonUser = types.ReplyKeyboardMarkup()
		buttonUser.add(types.KeyboardButton('Подробная информация о пользователе'), types.KeyboardButton('Выход')) 
		msg = bot.send_message(message.chat.id, "Выберите, что хотите сделать дальше: ", reply_markup=buttonUser)

		bot.register_next_step_handler(msg, user_check)

def user_check_other_user(message):
	name = message.text

	bot.send_message(message.chat.id, showUsersName(name))
	bot.send_message(message.chat.id, showUsersGroup(name))								
	msg = bot.send_message(message.chat.id, showUsersDescription(name))

	buttonUser = types.ReplyKeyboardMarkup()
	buttonUser.add(types.KeyboardButton('Подробная информация о другом пользователе'), types.KeyboardButton('Выход')) 
	msg = bot.send_message(message.chat.id, "Выберите, что хотите сделать дальше: ", reply_markup=buttonUser)
	
	bot.register_next_step_handler(msg, user_check)


def user_showСompan(message):
	bot.send_message(message.chat.id, companyInfo())
	buttonUser = types.ReplyKeyboardMarkup()

	buttonUser.add(types.KeyboardButton('Обучение профессии'), types.KeyboardButton('Посмотреть коллег'), types.KeyboardButton('О компании'), types.KeyboardButton('Настройки'), types.KeyboardButton('Выход')) 
	msg = bot.send_message(message.chat.id, "Выберите, что хотите сделать дальше: ", reply_markup=buttonUser)

	bot.register_next_step_handler(msg, user_answer2)


def settings(message):
	if(message.text == "Изменить информацию о себе"):
		msg = bot.send_message(message.chat.id, "Введите персональный код для подтверждения: ")
		bot.register_next_step_handler(msg, settings2)
	elif(message.text == "Выйти"):
		buttonUser = types.ReplyKeyboardMarkup()

		buttonUser.add(types.KeyboardButton('Обучение профессии'), types.KeyboardButton('Посмотреть коллег'), types.KeyboardButton('О компании'), types.KeyboardButton('Настройки'), types.KeyboardButton('Выход')) 
		msg = bot.send_message(message.chat.id, "Выберите, что хотите сделать дальше: ", reply_markup=buttonUser)

		bot.register_next_step_handler(msg, user_answer2)
	else: 
		bot.send_message(message.chat.id, "Такого варианта нет ")
		buttonsettings = types.ReplyKeyboardMarkup()

		buttonsettings.add(types.KeyboardButton('Изменить информацию о себе'), types.KeyboardButton('Выйти'))
		msg = bot.send_message(message.chat.id, "Вот возможные настройки: ", reply_markup=buttonsettings)

		bot.register_next_step_handler(msg, settings)

def settings2(message):
	a = message.text
	if (vabalabda(a) == [(1,)]): 
		msg = bot.send_message(message.chat.id, "Введите новое описание: ")
		bot.register_next_step_handler(msg, settings3, a)
	else:
		ssg = bot.send_message(message.chat.id, "Неверный персональный код ")
		buttonsettings = types.ReplyKeyboardMarkup()

		buttonsettings.add(types.KeyboardButton('Изменить информацию о себе'), types.KeyboardButton('Выйти'))
		msg = bot.send_message(message.chat.id, "Вот возможные настройки: ", reply_markup=buttonsettings)

		bot.register_next_step_handler(msg, settings)

def settings3(message, a):
	name = message.text
	addDescription(name, a)
	print(addDescription(name, a))
	bot.send_message(message.chat.id, "Описание успешно сохранено")
	buttonsettings = types.ReplyKeyboardMarkup()

	buttonsettings.add(types.KeyboardButton('Изменить информацию о себе'), types.KeyboardButton('Выйти'))
	msg = bot.send_message(message.chat.id, "Выберите, что хотите сделать дальше: ", reply_markup=buttonsettings)

	bot.register_next_step_handler(msg, settings)


bot.enable_save_next_step_handlers(delay=12)
bot.load_next_step_handlers()
#Врубаем бота
bot.polling()
