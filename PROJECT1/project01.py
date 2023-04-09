import sqlite3 as s
conn=s.connect('Project1.sqlite')
cur=conn.cursor()

qry=''' CREATE TABLE DEPT(
    DEPTNO NUMBER(2) NOT NULL, 
    DNAME VARCHAR(14),
    LOC VARCHAR(13)
);

'''
try:
    cur.execute(qry)
    conn.commit()
    print("Table created successfully.")

except Exception as e:
    print("failed to do so.",e)

conn.close()

