import sqlite3 as sq

with sq.connect("Base.db", check_same_thread=False) as con:
	cur = con.cursor()

	cur.execute("""CREATE TABLE IF NOT EXISTS users (
		userid INTEGER NOT NULL,
		name TEXT NOT NULL,
		group_ TEXT NOT NULL,
		progress INTEGER DEFAULT 0,
		description TEXT DEFAULT "Нет информации"
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
		cur.execute("SELECT count(userid) FROM users WHERE userid = ?", [params])
		result = cur.fetchall()
		return result


	def getIds():
		cur.execute("SELECT userid FROM users")
		ids = []
		res = cur.fetchall()
		for i in range(len(res)):
			ids.append(res[i][0])
		return ids	


def showUsersName(name):
	return f"""
	Имя: {name}	
	
	"""

def showUsersGroup(name):
		params = (name)
		cur.execute("SELECT group_ FROM users WHERE name = ?", [params])
		result = cur.fetchall()
		return f"""
		Группа: {result[0][0]}
		
	"""

def showUsersDescription(name):
		params = (name)
		cur.execute("SELECT description FROM users WHERE name = ?", [params])
		result = cur.fetchall()
		return f"""
		Описание: {result[0][0]}
		
	"""


registerUser(2, "boobs", "man")
#addDescription("fdsfdsfdsfdshhjkfghiuvhjkdvnuie", 12)
#print(showUsers())
#print(getIds())
