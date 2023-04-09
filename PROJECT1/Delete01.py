import sqlite3 as s
conn=s.connect('Project1.sqlite')
cur=conn.cursor()

try:
    cur.execute("DELETE FROM DEPT WHERE LOC = 'KOLKATA';")
    conn.commit()
    print("Row Deleted Successfully.")

except Exception as e:
    print("task failed",e)

conn.close()