from base import registerUser
from base import showUsers
from base import addDescription
from random import randint

def addUserButton():
	return "Введите данные: "

def deleteUserButton(): pass

def showUsersData(): pass

def createAnnounse(): pass

def chatWithUser(): pass


def addUser(name, group):
	registerUser(randint(10000000, 99999999), name, group)
	return f"""
	Пользователь зарегестрирован
	id: {userid}
	Имя: {name}

	"""
