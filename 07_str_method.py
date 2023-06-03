class Person:
    def __init__(self, name):
        self.name = name
    
    def __str__(self) -> str:
        return self.name

csaba = Person("Kiss Csaba")
tamas = Person("Nagy Csaba")
csilla = Person("Kovács Csilla")

print(csaba)
print(tamas)
print(csilla)