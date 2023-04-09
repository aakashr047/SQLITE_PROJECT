import sqlite3 as s
conn=s.connect('Project1.sqlite')
cur=conn.cursor()

id=int(input("Enter DEPT NO: "))
depn= input("Enter DEPT NAME: ")
loc=input("Enter location: ")

try:
    cur.execute("INSERT INTO DEPT VALUES(?,?,?);",(id,depn,loc))
    conn.commit()
    print("Mission accomplished.!")

except Exception as e:
    print("Task failed",e)


conn.close()