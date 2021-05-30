#Inheritance

class Person:
    
    def __init__(self,name,age):
        self.name=name
        self.age=age
    
    def get_name(self):
        return self.name

    def greeting(self):
        return f"Hello {self.name}"
    
    def get_age(self):
        return self.age
    
    def __str__(self):
        return f"{self.name} has an age of {self.age} years"

class Student:
    
    def __init__(self,name,age,standard):
        super().__init__(name,age)
        self.standard=standard
    
    def greeting(self):
        return f"Hello student {self.name}"
    
    def __str__(self):
        super().__str__('Student')
        return f"You are in class {self.standard}"


harry=Person("Harry",10)
print(harry)
print(harry.get_name())
print(harry.greeting())

ron=Student("Ron",15,6)
print(ron)