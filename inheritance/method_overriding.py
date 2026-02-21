class Person:
    def speak(self):
        print("Hello")

class Student(Person):
    def speak(self):
        print("I am a student")

s = Student()
s.speak()