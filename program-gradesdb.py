#program X - students grade computation using SQLite3 database

import sqlite3
path=r'C:\Users\humer\PycharmProjects\python-exercises\gradesdb.db'
con=sqlite3.connect(path)
roll = input('Enter roll no ')
name = input('Enter name ')
print('Enter Marks ')
s1=int(input('java '))
s2=int(input('C '))
s3=int(input('c++ '))
s4=int(input('dbms '))
s5=int(input('os '))

q='''insert into gradesta values(?,?,?,?,?,?,?);'''
cur=con.cursor()
cur.execute(q,(roll,name,s1,s2,s3,s4,s5))
con.commit()

q='select * from gradesta where roll=:roll;'
c=con.cursor()
c.execute(q,{"roll":roll})
rec=c.fetchone()


tot=rec[2] + rec[3] + rec[4] + rec[5] + rec[6]
print(tot)
avg=tot / 5
'''if (s1 < 50 or s2 < 50 or s3 < 50 or s4 < 50 or s5 < 50):
    print('Grade F')
    quit()'''
if(avg >= 90):
    print('Grade A')
elif(avg >= 80 ):
    print("Grade B")
elif(avg >= 70 ):
    print('Grade C')
elif(avg >= 60 ):
    print('Grade D')
elif(avg >= 50 ):
    print('Grade E')
else:
    print('Grade F')

