# All classes have a function called __init_(), which is always executed when the object is being initiated.

class Student:
    def __init__(self,name):   #self is 
        self.name = name
        print("Creating New function")

s1 = Student("Jitendra")  # This will call the __init__ method
print(s1.name)

s2 = Student("Shubhman")
print(s2.name)