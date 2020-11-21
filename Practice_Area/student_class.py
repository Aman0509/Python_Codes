class Student:

    def __init__(self, name, rollno):
        self.name = name
        self.rollno = rollno
        self.age = 0
        self.marks = 0

    def setAge(self, age):
        self.age = 0

    def setMarks(self, marks):
        self.marks = marks

    def display(self):
        print("Student Detail".center(48, "*"))
        print("Roll No - ", self.rollno)
        print("Name - ", self.name)
        print("Age - ", self.age)
        print("Marks - ", self.marks)


obj1 = Student('Adarsh', 1)
obj1.setMarks(89)
obj1.setAge(17)
obj1.display()
