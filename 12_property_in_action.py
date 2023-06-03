class Student:
    def __init__(self, first_name, last_name):
        self.__first_name = first_name
        self.__last_name = last_name
        self.__marks = []

    @property
    def full_name(self):
        return f"{self.__first_name} {self.__last_name}"
    
    @property
    def average(self):
        return sum(self.__marks) / len(self.__marks)

    def set_mark(self, new_mark):
        self.__marks.append(new_mark)
    
    def __str__(self) -> str:
        return self.full_name
    

csaba = Student("Kiss", "Csaba")
csaba.set_mark(5)
csaba.set_mark(3)
csaba.set_mark(2)
csaba.set_mark(1)
print(csaba.average)