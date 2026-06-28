# class Person:
#     def __init__(self , n , s):
#         self.name=n
#         self.Std=s
   
#     def info(self):
#         print(self.name ,"is studying at",self.Std )

# class School(Person):
#     def showLanguage(self):
#         print("python")
        
   
# a=Person("Ajay","3rd year") 
# b=School("tara", "4th year")

# a.info()
# b.info()
# b.showLanguage()

#heritance - Single heritance + Polymorphism

# class Animal:
#     def __init__(self,name):
#         self.name=name

# class dog(Animal):
#     def sound(self):
#         print(self.name ,"bark")

# class cat(Animal):
#     def sound(self):
#         print(self.name ,"meow")

# b=dog("dog")
# b.sound()

# c=cat("Cat")
# c.sound()

#Encapsulation

# class Student:
#     def __init__(self,name):
#         self.name= name
    
#     def display(self):
#         print(self.name)



# s=Student("Ajay")
# s.display
    
#     def __init__(self,name):
#         self._name= name
    

# a=Student("Ajay")
# print(a._name
from abc import ABC,abstractmethod

class Banking(ABC):

    def database(self):
        print("database")
    
    @abstractmethod
    def security(self):
        pass


class Mobile(Banking):

    def login(self):
        print("login")

    def security(self):
        print("Security")

mob=Mobile()
mob.login()
mob.security()