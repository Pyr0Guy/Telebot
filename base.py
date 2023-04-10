import sqlite3 as sq

with sq.connect("Base.db") as con:
	cur = con.cursor()

	cur.execute("""CREATE TABLE IF NOT EXISTS users (
		userid INTEGER PRIMARY KEY AUTOINCREMENT,
		name TEXT NOT NULL,
		group TEXT DEFAULT NULL, #admin, employee
		telegramlink TEXT NOT NULL
		)""")


	def registerUser(name, telegramlink):
		#cur.execute("INSERT INTO users()")
		pass
