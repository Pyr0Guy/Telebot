import sqlite3 as sq

with sq.connect("Base.db") as con:
	cur = con.cursor()

	cur.execute("""CREATE TABLE IF NOT EXISTS users (
		userid INTEGER NOT NULL,
		name TEXT NOT NULL,
		group TEXT NOT NULL, #admin, employee
		progress INTEGER DEFAULT 0
		)""")


	def registerUser(Userid, Name, Group, Progress=0):
		cur.execute(f"INSERT INTO users (userid, name, group, progress) VALUES({Userid}, {Name}, {Group}, {Progress})")
		pass

#registerUser(3434, "fdsfs", "employee")
