from base import getIds

userGroup = None
tryes = 0
def adminButton():
	return "Введите пароль"

def adminAuth(password):
	if password == "123":
		userGroup = "admin"
		return "Добро пожаловать"
	else:
		return "Пароль не правильный" 

def employeeButton():
	return "Введите персональный код: "

def employeeAuth(id):
	if id in getIds():
		userGroup = "employee"
		return "Добро пожаловать"
