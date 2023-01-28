import mysql.connector
import datetime


def getProductInfo():
    connection = mysql.connector.connect(host="localhost", user="root", password="pasapasaword", database="node-app")
    cursor = connection.cursor()
    # sql = "Select count(*) from products where price >2000"

    sql = "Select AVG(price) from products"
    sql = "Select SUM(price) from products"
    sql = "Select MIN(price) from products"
    sql = "Select MAX(price) from products"
    sql = "Select Name,price from products Where price = (Select MAX(price) from products)"

    cursor.execute(sql)

    result = cursor.fetchone()

    print(result)
    # print(f"Id = {result[0]},\nName: {result[1]},\nPrice: {result[2]}\n")

@staticmethod
def getStudentInfo():
    connection = mysql.connector.connect(host="localhost", user="root", password="passwrd",
                                         database="schooldatabase")
    cursor = connection.cursor()

    sql = "Select StudentNumber,name,surname from student"
    sql = "Select name,surname from student where gender ='K' "
    sql  ="Select name surname from student where YEAR(birthdate)=2003"
    sql = "Select name,surname from student where name LIKE '%an%' OR surname LIKE '%an%' "
    sql = "Select name,surname from student where name='ali' and YEAR(birthdate)=2005 "
    sql = "Select name from student where gender = 'K' order by name "
    sql = "Select count(*) from student where gender = 'E'"
    sql = "Select * from student"

    cursor.execute(sql)
    try:
        result = cursor.fetchall()
        for i in result:
            print(i)
    except mysql.connector.Error as err:
        print("Error: "+err)
    finally:
        connection.close()



getStudentInfo()
