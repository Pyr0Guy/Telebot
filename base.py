import sqlite3 as sq

with sq.connect("Base.db", check_same_thread=False) as con:
	cur = con.cursor()

	cur.execute("""CREATE TABLE IF NOT EXISTS users (
		userid INTEGER NOT NULL,
		name TEXT NOT NULL,
		group_ TEXT NOT NULL,
		progress INTEGER DEFAULT 0,
		description TEXT NOT NULL
		)""")


	def registerUser(Userid, Name, Group, Progress=0):
		params = (Userid, Name, Group, Progress, None)
		cur.execute("INSERT INTO users VALUES (?,?,?,?,?)", params)
		return Userid

	def addDescription(Text, Userid):
		params = (Text, Userid)
		cur.execute("UPDATE users SET description=? WHERE userid=?", params)

	def showUsers():
		cur.execute("SELECT name, userid, group_, description FROM users")
		result = cur.fetchall()
		return result

	def vabalabda(id):
		params = (id)
#<<<<<<< HEAD
#		cur.execute("SELECT count(userid) FROM users WHERE userid = ?", (params,))
#=======
		cur.execute("SELECT count(userid) FROM users WHERE userid = ?", [params])
#>>>>>>> c91899cc9d8922ad01a6115be6b8df35e81559ab
		result = cur.fetchall()
		return result

	def getIds():
		cur.execute("SELECT userid FROM users")
		ids = []
		res = cur.fetchall()
		for i in range(len(res)):
			ids.append(res[i][0])
		return ids
	
	def showUsersNAME(name):
		params = (name)
		cur.execute("SELECT name, group_, description FROM users WHERE name = ?", params)
		result = cur.fetchall()
		return f"""
		Пользователь зарегестрирован
		Имя: {name}

	"""

	def updateProgress(Userid):
		params = (Userid)
		cur.execute("UPDATE users SET progress = progress + 1 WHERE userid=?", params)

	def showUsersNAME(name):
		params = (name)
		cur.execute("SELECT name, group_, description FROM users WHERE name = ?", [params])
		result = cur.fetchall()
		return f"""
		Имя: {name}
		
	"""


registerUser(2, "boobs", "man")
#addDescription("fdsfdsfdsfdshhjkfghiuvhjkdvnuie", 12)
#print(showUsers())
#print(getIds())
