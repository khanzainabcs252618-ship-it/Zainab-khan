import sqlite3
connection = sqlite3.connect("MVLU CS department")
print(connection.total_changes)

# Step 2: Adding table into Database
cursor = connection.cursor()
cursor.execute("CREATE TABLE IF NOT EXISTS student3 (rollno int, name varchar(20), class varchar(10), course varchar(20))")
connection.commit()
print("student3 table created")

# Step 3: Insert values
cursor.execute("INSERT INTO student3 VALUES (1, 'Zainab', 'FYCS', 'CS')")
connection.commit()
print("Value inserted successfully")

cursor.execute("INSERT INTO student3 VALUES (2, 'Priya', 'FYCS', 'CS')")
connection.commit()
print("Value inserted successfully")

cursor.execute("INSERT INTO student3 VALUES (3, 'Anam', 'FYCS', 'CS')")
connection.commit()
print("Value inserted successfully")

cursor.execute("INSERT INTO student3 VALUES (4, 'Dia', 'FYCS', 'CS')")
connection.commit()
print("Value inserted successfully")

cursor.execute("INSERT INTO student3 VALUES ('5', 'Sara', 'FYCS', 'CS')")
connection.commit()
print("Value inserted successfully")

#Step4: Update value in database
from sqlite3 import *
connection = connect("MVLU CS department")
cur = connection.cursor()
connection.execute("update student3 set rollno = 6 where name = 'Sara'")
connection.commit()
print("Total No.of row updated")
connection.close

#Step5: Select value in database
from sqlite3 import *
connection = connect('MVLU CS department')
cur = connection.cursor()
data = connection.execute("select * from student3")
print(type(data))
for record in data:
    print("name:",record[0])
    print("rollno:",record[1])
    print("class:",record[2])
    print("course:",record[3])
    print("##"*25)
connection.close

Connection = connect('MVLU CS department')
cur = connection.cursor()
val = [(1, 'Zainab', 'FYCS', 'CS'), (2, 'Priya', 'FYCS', 'CS'), (3, 'Anam', 'FYCS', 'CS'), (4, 'Dia', 'FYCS', 'CS'), ('5', 'Sara', 'FYCS', 'CS')]
cur.executemany("insert into student3 values(?,?,?,?)",val)
print("Multi data")
connection.commit()
connection.close()



































