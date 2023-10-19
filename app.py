from Dbmanager import DbManger
import datetime
from Student import Student
class App:
    def __init__(self):
        self.db = DbManger()
        pass
    def initApp(self):
        msg = "******\n1-)Öğrenci Listesi\n2-)Öğrenci Ekle\n3-)Öğrenci Güncelle\n4-)Öğrenci Sil\n5-)Öğretmen Ekle\n6-)Sınıflara Göre Dersler\n7-)Çıkış(E/Ç)"    
        while True:
            print(msg)
            islem = input("Seçim: ")
            if islem == "1":
                self.displayStudents()
            elif islem == "2":
                self.addStudent()
            elif islem == "3":
                self.editStudent()
            elif islem == "4":
                self.deleteStudent()
            elif islem == "5":
                pass
            elif islem == "6":
                pass
            elif islem == "E" or islem == "C":
                break
            else:
                print("Yanlış Seçim ...")
    def editStudent(self):
        classid = self.displayStudents()
        studentid = int(input("Öğrenci İd : "))
        student = self.db.getStudentById(studentid)

        student[0].surname = input("Yeni Ad : ") or student[0].surname ## Burda herhangi bir girilmezzse or surname aynen kalsın demiş olduk 
        student[0].lastname = input("Yeni Soyad : ") or student[0].lastname
        student[0].classId = input("Yeni ClassId : ") or student[0].classId
        student[0].gender = input("Yeni Gender E/K : ") or student[0].gender

        year = input("Doğum Yılı : ") or student[0].birtdate.year
        month = input("Öğreni Ay :") or student[0].birtdate.month
        day = input("Öğrenici Gün ") or student[0].birtdate.day
        
        student[0].birtdate = datetime.datetime(year,month,day)
        
        self.db.editStudent(student[0])
        

    def SınıfListele(self):
        classes = self.db.getClass()
        for i in classes:
            print(f"{i.id}:{i.Name}")       
    
    def displayStudents(self):
        self.SınıfListele()
        classid = int(input("Hangi Sınıf : "))
        students =self.db.getStudentsByClassId(classid)
        print("Öğrenci Listesi")

        for std  in students:
            print(f"{std.id}:{std.surname} 1{std.lastname}")
        return classid    

    def addStudent(self):

        self.SınıfListele()
        classid = int(input("Hangi Sınıf : "))
        number = input("Ogrenci Numarası : ")
        name = input("Öğrenci İsmi : ")
        lastname = input("Öğrenci Soyad : ")
        year = int(input("Doğum Yılı : "))
        month = int(input("Öğreni Ay :"))
        day = int(input("Öğrenici Gün "))
        birhtdate = datetime.datetime(year,month,day)
        gender = input("Öğrenci Cinsiyet (E/K) : ")

        student = Student(None,number,name,lastname,birhtdate,gender,classid)
        self.db.addStudent(student) 

    def deleteStudent(self):
        classid = self.displayStudents()
        studentid = int(input("Öğrenci İd : "))
        self.db.DeleteStudent(studentid)        
app = App()
app.initApp()