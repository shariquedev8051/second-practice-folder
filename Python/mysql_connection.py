import mysql.connector

mydb = mysql.connector.connect(
    host='localhost',
    user = 'root',
    password = 'root',
    database = 'test_db'
    )

mycursor = mydb.cursor()
# mycursor.execute('Create database test_db') # datbase created with name test_db
mycursor.execute('CREATE TABLE test(id INT AUTO_INCREMENT PRIMARY KEY, name VARCHAR(255))') 