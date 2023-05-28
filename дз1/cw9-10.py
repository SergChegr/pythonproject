# import sqlite3
#
# connection = sqlite3.connect("itstep_DB.sl3", 5)
#
# cur = connection.cursor()
#
# print(connection)
# print(cur)
# connection.close()

# import sqlite3
#
# connection = sqlite3.connect("D:\\itstep_DB.sl3", 5)
# cur = connection.cursor()
# cur.execute("CREATE TABLE first_table (name TEXT);")
# connection.commit()
# connection.close()

# import sqlite3
#
# connection = sqlite3.connect("D:\\itstep_DB.sl3", 5)
# cur = connection.cursor()
# cur.execute("INSERT INTO first_table (name) VALUES ('Nick');")
# connection.commit()
# connection.close()

# import sqlite3
#
# connection = sqlite3.connect("D:\\itstep_DB.sl3", 5)
# cur = connection.cursor()
# cur.execute("INSERT INTO first_table (name) VALUES ('Danil')")
# cur.execute("INSERT INTO first_table (name) VALUES ('Sergey')")
# cur.execute("INSERT INTO first_table (name) VALUES ('Roman')")
# cur.execute("SELECT rowid, name FROM first_table WHERE rowid=3;")
# connection.commit()
# cur.execute("DELETE FROM first_table WHERE rowid=3;")
# connection.commit()
# res = cur.fetchall()
# print(res)
# connection.close()
