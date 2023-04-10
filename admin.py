from base import registerUser

def addUserButton():
	return "Введите данные: "

def deleteUserButton(): pass

def showUserData(): pass

def createAnnounse(): pass

def chatWithUser(): pass


def addUser(userid, name, group):
	registerUser(userid, name, group)
	return f"""
	Пользователь зарегестрирован
	id: {userid}
	Имя: {name}

	"""