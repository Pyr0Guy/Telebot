userGroup = None
tryes = 0

def adminButton():
	return "Введите пароль"

def adminAuth(password):
	if password == "123":
		userGroup = "admin"
		return "Добро пожаловать"
	else:
		tryes += 1
		return f"Пароль не правильный повторите вход у вас осталось {3 - tryes} попытки" 

def employeeButton():
	return "Введите персональный код: "

def employeeAuth():
	pass

