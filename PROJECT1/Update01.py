import sqlite3 as s
conn=s.connect('Project1.sqlite')
cur=conn.cursor()

try:
    cur.execute("UPDATE DEPT SET LOC = 'KOLKATA' WHERE DEPTNO = 200")
    conn.commit()
    print("Table created successfully.")

except Exception as e:
    print("task failed",e)

conn.close()