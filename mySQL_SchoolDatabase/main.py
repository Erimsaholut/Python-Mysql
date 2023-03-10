import statistics

import mysql.connector
from datetime import datetime
from connection import connection


class Student:
    connection = connection
    mycursor = connection.cursor()

    def __init__(self, id, studentNumber, name, surname, birthdate, gender):
        if id is None:
            self.id = 0
        else:
            self.id = id
        self.studentNumber = studentNumber
        self.name = name
        self.surname = surname
        self.birtdate = birthdate
        self.gender = gender

    def saveStudent(self):
        sql = "INSERT INTO STUDENT(StudentNumber,Name,Surname,Birthdate,Gender) VALUES(%s,%s,%s,%s,%s)"
        values = (self.studentNumber, self.name, self.surname, self.birtdate, self.gender)
        Student.mycursor.execute(sql, values)
        try:
            Student.connection.commit()
            print(f"{Student.mycursor.rowcount} Data added.")
        except mysql.connector.Error as err:
            print("Error", err)
        finally:
            Student.connection.close()

    @staticmethod
    def saveStudents(students):
        sql = "INSERT INTO STUDENT(StudentNumber,Name,Surname,Birthdate,Gender) VALUES(%s,%s,%s,%s,%s)"
        values = students
        Student.mycursor.executemany(sql, values)
        try:
            Student.connection.commit()
            print(f"{Student.mycursor.rowcount} Data added.")
        except mysql.connector.Error as err:
            print("Error", err)
        finally:
            Student.connection.close()

    def updateStudentByStudentNumber(self):
        sql = "Update student from student set name=%s,id=%s where studentNumber=%s "
        values = self.name, self.id, self.studentNumber,
        Student.mycursor.execute(sql, values)

        try:
            Student.connection.commit()
            print(f"{Student.mycursor.rowcount} Data updated.")
        except mysql.connector.Error as err:
            print("Error", err)
        finally:
            Student.connection.close()


Student.updateStudentByStudentNumber()

ahmet = Student("101", "Ahmet", "Y??lmaz", datetime(2005, 5, 17), "E")
# ahmet.saveStudent()
students = [
    ("201", "Ahmet", "Y??lmaz", datetime(2005, 5, 17), "E"),
    ("202", "Ali", "Can", datetime(2005, 6, 17), "E"),
    ("203", "Canan", "Tan", datetime(2005, 7, 7), "K"),
    ("204", "Ay??e", "Taner", datetime(2005, 9, 23), "K"),
    ("205", "Bahad??r", "Toks??z", datetime(2004, 7, 27), "E"),
    ("206", "Ali", "Cenk", datetime(2003, 8, 25), "E")
]
# Student.saveStudents(students)
