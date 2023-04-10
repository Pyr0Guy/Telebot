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


	def registerUser(Userid, Name, Group Progress=0,):
		params = (Userid, Name, Group, Progress)
		cur.execute("INSERT INTO users VALUES (?,?,?,?)", params)
		pass

#registerUser(12 ,"fdsfshfghf", "employee", 0)
