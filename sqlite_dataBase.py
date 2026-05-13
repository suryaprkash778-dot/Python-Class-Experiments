import sqlite3
conn = sqlite3.connect("record.db")
cur = conn.cursor()

student = """CREATE TABLE IF NOT EXISTS STUDENTS
(STUDENT_ROLL_NO INTEGER PRIMARY KEY AUTOINCREMENT,
STUDENT_NAME VARCHAR(255) NOT NULL,
STUDENT_CLASS VARCHAR(255) NOT NULL,
STUDENT_EMAIL VARCHAR(255) NOT NULL,
STUDENT_PH_NO INTEGER NOT NULL)"""

cur.execute(student)

while True:
    var1= input("enter name :")
    var2= input("enter grade :")
    var3= input("enter email :")
    var4= input("enter phone number :")

    t= (var1,var2,var3,var4)

    student_1 = """INSERT INTO STUDENTS
    (STUDENT_NAME, STUDENT_CLASS, STUDENT_EMAIL, STUDENT_PH_NO)
    VALUES(?,?,?,?)"""
    yes_no = input("do you want to add more data (yes/no)")
    cur.execute(student_1, t)
    if yes_no == "no" or yes_no=="NO":
        break

get_data = conn.execute("SELECT * FROM STUDENTS LIMIT (3) ") # to fetch the data, we use select query
for i in get_data:# GIVES A LIST OF TUPLES OF DATA, SO WE ARE LOOPING OVER THEM
    print(i)

conn.execute("DELETE FROM STUDENTS WHERE STUDENT_ROLL_NO = 3")# QUERY FOR DELETING A PARTICULAR ROW

conn.execute("UPDATE STUDENTS SET STUDENT_PH_NO = 1, STUDENT_NAME = 'JOHN'"
             ""
             " WHERE STUDENT_ROLL_NO = 2")#QUERY TO UPDATE DATA

conn.commit()
conn.close()



