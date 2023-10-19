import mysql.connector
from datetime import datetime
from Baglantı import baglantı
from Student import Student
from Teacher import Teacher
from Class import Class

class DbManger:
    def __init__(self):
        self.baglantı = baglantı
        self.cursor = self.baglantı.cursor()

    def getStudentById(self,id):
        sql = "select * from student where id = %s "
        value =(id,)
        self.cursor.execute(sql,value)
        try:
            obj = self.cursor.fetchone()  
            return Student.CreatStudent(obj)
            
        except mysql.connector.Error as err:
            print("hata",err)
           
    def getClass(self):
        sql = "Select * from class"
        self.cursor.execute(sql)

        try:
            obj = self.cursor.fetchall()
            return Class.CreatClass(obj)
        except mysql.connector.Error as err:
            print("Hata",err)      
        

    def getStudentsByClassId(self,id):
        sql = "select * from student where classId = %s "
        value =(id,)
        self.cursor.execute(sql,value)
        try:
            obj = self.cursor.fetchall()
            return Student.CreatStudent(obj)
        except mysql.connector.Error as err:
            print("hata",err)
        finally:
            
            print("DataBase Bağlantısı Kapatıldı ") 

    
    def addStudent(self,student : Student):
        SqlQuery = "INSERT INTO student(number,surname,lastname,birtdate,gender,classId)VALUES(%s,%s,%s,%s,%s,%s)"
        Values = (student.number,student.surname,student.lastname,student.birtdate,student.gender,student.classId)
        self.cursor.execute(SqlQuery,Values)
        try:
            self.baglantı.commit()

            
            print(f"{self.cursor.rowcount} Tane Kayıt Eklendi")
            
        except mysql.connector.Error as err:
            print("hata",err)
      

    def editStudent(self,student:Student):
        SqlQuery = "Update student set number =%s ,surname=%s,lastname=%s,birtdate=%s,gender=%s ,classId=%s where id=%s"
        Values = (student.number,student.surname,student.lastname,student.birtdate,student.gender,student.classId,student.id)
        self.cursor.execute(SqlQuery,Values)
        try:
            self.baglantı.commit()
            
            print(f"{self.cursor.rowcount} Tane Kayıt Güncellendi")
            
        except mysql.connector.Error as err:
            print("hata",err)

    def DeleteStudent(self,studentId):
        sql = "delete  from student where id= %s"
        Value = (studentId,)
        self.cursor.execute(sql,Value)

        try:
            self.baglantı.commit()
            print(f"{self.cursor.rowcount} adet Kayıt Silindi ")
        except  mysql.connector.Error as err:
            print("Hata",err)

    def addTeacher(self,teacher:Teacher):
        pass    

    def aditTeacher(self,teacher:Teacher):
        pass  
    
        
