#Inheritance

class Person:
    
    def __init__(self,name,age):
        self.name=name
        self.age=age
    
    def get_name(self):
        return self.name

    def greeting(self):
        print( f"Hello {self.name}")
    
    def get_age(self):
        return self.age
    
    def __str__(self):
        return f"{self.name} has an age of {self.age} years"

class Student(Person):
    
    def __init__(self,name,age,standard):
        super().__init__(name,age)
        self.standard=standard
    
    def greeting(self):
        
        print( f"Hello student {self.name}")
        super().greeting()
    
    def __str__(self):
        super().__str__()
        return f"You are in class {self.standard}"
    
    def double_of_age(self):
        return self.age*2

class Prefect(Student):
    
    def __init__(self,name,age,standard,house):
        super().__init__(name,age,standard)
        self.house=house
        
    def greeting(self):
        super().__str__()
        print(f"Hello Prefect {self.name}")
    
    def age_double_std(self):
        return super().double_of_age() + self.standard

harry=Person("Harry",10)
print(harry)
print(harry.get_name())
print(harry.greeting())

ron=Student("Ron",15,6)
print(ron)
ron.greeting()
print(ron.double_of_age())

john=Prefect("John",23,10,"green")
john.greeting()
print(john.age_double_std())