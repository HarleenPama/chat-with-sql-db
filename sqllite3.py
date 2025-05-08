import sqlite3


# Connect to sqlite 
connection = sqlite3.connect("Student.db")

# create a cursor object to insert record, connect table

cursor = connection.cursor()

# create table
table_info = """
create table STUDENT(NAME VARCHAR(25), CLASS VARCHAR(25), SECTION VARCHAR(25), MARKS INT)"""

cursor.execute(table_info)

# insert some more records

cursor.execute('''insert into STUDENT values('Rahul', '10', 'A', 90)''')
cursor.execute('''insert into STUDENT values('Rohit', '10', 'B', 80)''')
cursor.execute('''insert into STUDENT values('Raj', '10', 'A', 85)''')
cursor.execute('''insert into STUDENT values('Ravi', '10', 'B', 95)''')

# display the results
print("Inserted records are")
data = cursor.execute('''Select * from STUDENT''')

for row in data:
    print(row)

# Commit changes in the database
connection.commit()
connection.close()