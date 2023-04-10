import sqlite3 as sq

with sq.connect("Base.db") as con:
	cur = con.cursor()

	cur.execute("""CREATE TABLE IF NOT EXISTS users (
		userid INTEGER NOT NULL,
		name TEXT NOT NULL,
		group_ TEXT NOT NULL,
		progress INTEGER DEFAULT 0,
		description TEXT
		)""")


	def registerUser(Userid, Name, Group, Progress=0):
		params = (Userid, Name, Group, Progress, None)
		cur.execute("INSERT INTO users VALUES (?,?,?,?,?)", params)

	def addDescription(Text, Userid):
		params = (Text, Userid)
		cur.execute("UPDATE users SET description=? WHERE userid=?", params)

	def showUsers():
		cur.execute("SELECT * FROM users")
		result = cur.fetchall()
		return result

#registerUser(12 ,"fdjsfshfghf", "employee", 0)
#addDescription("fdsfdsfdsfdshhjkfghiuvhjkdvnuie", 12)
#print(showUsers())

