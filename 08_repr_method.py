class Person:
    def __init__(self, name, email, address):
        self.name = name
        self.email = email
        self.address = address
    
    def __str__(self) -> str:
        return f"Name: {self.name} Email: {self.email} Address: {self.address}"
    
    def __repr__(self) -> str:
        return self.name

csaba = Person("Kiss Csaba", "csaba@gmail.com", "Pécs")
tamas = Person("Nagy Csaba", "tamas@gmail", "Budapest")
csilla = Person("Kovács Csilla", "csilla@gmail", "Debrecen")

my_friends = [csaba, tamas, csilla]
print(my_friends)
print(csaba)
print(tamas)
print(csilla)