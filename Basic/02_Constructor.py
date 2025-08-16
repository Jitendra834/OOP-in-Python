# All classes have a function called __init_(), which is always executed when the object is being initiated.

class Student:
    def __init__(self,name,age):   #self is a  
        self.name = name
        self.age = age
        print("Creating New function")

s1 = Student("Jitendra",21)  # This will call the __init__ method
print(s1.name,s1.age)

s2 = Student("Shubhman",34)
print(s2.name,s2.age)

# Advanced: Adding default values, type hints, and additional attributes

class AdvancedStudent:
    def __init__(self, name: str, age: int = 18, grade: str = "Freshman"):
        self.name = name
        self.age = age
        self.grade = grade
        self.courses = []
        print(f"Created AdvancedStudent: {self.name}, Age: {self.age}, Grade: {self.grade}")

    def enroll(self, course: str):
        self.courses.append(course)
        print(f"{self.name} enrolled in {course}")

    def info(self):
        return f"{self.name}, Age: {self.age}, Grade: {self.grade}, Courses: {', '.join(self.courses)}"

a1 = AdvancedStudent("Jitendra")
a1.enroll("Math")
a1.enroll("Science")
print(a1.info())

a2 = AdvancedStudent("Shubhman", 34, "Senior")
a2.enroll("History")
print(a2.info())