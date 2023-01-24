import mysql.connector

mydb=mysql.connector.connect(
    host="localhost", #192.31.45.65
    user="root",
    password = "*************",
    database = "mydatabase"
)
mycursor = mydb.cursor()

# mycursor.execute("SHOW DATABASES")
# mycursor.execute("CREATE DATABASE mydatabase")

# mycursor.execute("CREATE TABLE customers (name VARCHAR(255),address VARCHAR(255))")


