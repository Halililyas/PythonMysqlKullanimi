class Class:
    def __init__(self,id,Name,TeacherId):
        if id is None:
            self.id= 0
        else:
            self.id=id
        self.Name=Name  
        self.TeacherId = TeacherId  
    @staticmethod
    def CreatClass(obj):
        list =[]
        for i in obj:
            list.append(Class(i[0],i[1],i[2]))

        return list       