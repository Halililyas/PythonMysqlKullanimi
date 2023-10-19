class Student:
    def __init__(self,id,number,surname,lastname,birtdate,gender,classId):
        if id is None:
            self.id=0
        else:
            self.id = id 

        self.number =number
        self.surname= surname
        self.lastname =lastname
        self.birtdate=birtdate
        self.gender=gender
        self.classId=classId

    @staticmethod
    def CreatStudent(obj):
        list = []

        if isinstance(obj,tuple):
            list.append(Student(obj[0],obj[1],obj[2],obj[3],obj[4],obj[5],obj[6]))
        else:
            for i in obj:
                list.append(Student(i[0],i[1],i[2],i[3],i[4],i[5],i[6])) 
        
        return list    
