class Teacher:
    def __init__(self,id,Branch,Surname,Firstname,BirthDate,Gender):
        if id is None:
            self.id = 0
        else:
            self.id=id
        self.Branch = Branch
        self.Surname =Surname
        self.FirstName = Firstname
        self.BirthDate = BirthDate
        self.Gender = Gender
                