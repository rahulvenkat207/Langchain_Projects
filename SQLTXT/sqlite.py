import sqlite3

## Connect to sqllite

connection = sqlite3.connect("student.db")

## Create a cursor object to insert record,create table 

cursor = connection.cursor()

#create the table

table_info = """
  create table STUDENT(NAME VARCHAR(25),CLASS VARCHAR(25),
  SECTION VARCHAR(25),MARKS INT)
"""

cursor.execute(table_info)

# Insert records with different CLASS and SECTION values
cursor.execute('''INSERT INTO STUDENT VALUES ("Rahul", "Data Science", "A", 85)''')
cursor.execute('''INSERT INTO STUDENT VALUES ("Ranesh", "Full Stack", "A", 88)''')
cursor.execute('''INSERT INTO STUDENT VALUES ("Vishnu", "DevOps", "B", 90)''')
cursor.execute('''INSERT INTO STUDENT VALUES ("Priya", "Data Science", "A", 87)''')
cursor.execute('''INSERT INTO STUDENT VALUES ("Ranjith", "Full Stack", "B", 92)''')
cursor.execute('''INSERT INTO STUDENT VALUES ("Roshini", "DevOps", "A", 86)''')
cursor.execute('''INSERT INTO STUDENT VALUES ("Srika", "Data Science", "B", 89)''')
cursor.execute('''INSERT INTO STUDENT VALUES ("Jashera", "Full Stack", "A", 84)''')
cursor.execute('''INSERT INTO STUDENT VALUES ("Dafinia", "DevOps", "B", 91)''')
cursor.execute('''INSERT INTO STUDENT VALUES ("Srini", "Data Science", "A", 83)''')
cursor.execute('''INSERT INTO STUDENT VALUES ("Dhavamani", "Full Stack", "B", 82)''')
cursor.execute('''INSERT INTO STUDENT VALUES ("Daya", "DevOps", "A", 80)''')


##Display all the records
print("The inserted records are:")
data = cursor.execute('''Select * from STUDENT''')
for row in data:
    print(row)

# Commit the transaction
connection.commit()

# Close the connection
connection.close()

