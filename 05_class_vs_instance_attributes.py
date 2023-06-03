class Person:
    # class attribute
    country = "Hungary"
    number_of_people = 0

    def __init__(self, name):
        # instance attribute
        self.name = name
        Person.number_of_people += 1

csaba = Person("Kiss Csaba")
tamas = Person("Nagy Tamás")
edina = Person("Kovács Edina")
print(f"Name: {csaba.name} Country: {csaba.country} Population: {Person.number_of_people}")
print(f"Name: {tamas.name} Country: {tamas.country} Population: {Person.number_of_people}")
print(f"Name: {edina.name} Country: {edina.country} Population: {Person.number_of_people}")