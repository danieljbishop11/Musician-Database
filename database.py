import mysql.connector

mydb = mysql.connector.connect(
    host="localhost",
    user="root",
    passwd="123password",
    database="musiciandb"
)

mycursor = mydb.cursor()

sql = "ALTER TABLE producers CHANGE 'name' TO 'First Name'"

mycursor.execute(sql)

mydb.commit()

mydb.close()