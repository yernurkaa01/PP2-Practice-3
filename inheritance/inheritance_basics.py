class Person:
    def speak(self):
        print("Hello")

class Student(Person):
    pass

s = Student()
s.speak()