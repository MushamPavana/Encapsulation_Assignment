### Encapsulation :- Encapsulation is one of the fundamental principles of object-oriented programming (OOP).  
##It refers to the bundling of data (attributes) and the methods (functions) that operate on that data into a single unit known as a class. 
##Access to the data and methods is controlled, and only the necessary information is exposed to the outside world.

class Student:
    def __init__(self, name, age):
        self.name = name
        self.age = age
        
student1 = Student("pavana", 24)
student2 = Student("sneha", 22)
student3 = Student("swathi", 25)

print("Name:", student1.name)
print("Age:", student1.age)

print("Name:", student2.name)
print("Age:", student2.age)

print("Name:", student3.name)
print("Age:", student3.age)
