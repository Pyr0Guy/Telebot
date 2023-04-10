from base import registerUser
from random import randint

def addUserButton():
	return "Введите данные: "

def deleteUserButton(): pass

def showUserData(): pass

def createAnnounse(): pass

def chatWithUser(): pass


def addUser(name, group):
	registerUser(randint(1000000, 99999999), name, group)
	return f"""
	Пользователь зарегестрирован
	id: {userid}
	Имя: {name}

	"""