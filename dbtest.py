import sqlite3

dbp=r'C:\Users\humer\PycharmProjects\python-exercises\sqdbtest.db'
connection = sqlite3.connect(dbp)
c=connection.cursor()
q='select * from test;'
c.execute(q)
print(c.fetchall())
