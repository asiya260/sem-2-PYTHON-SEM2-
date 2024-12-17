class Student:
    def __init__(self, name, age, marks):
        self._name = name
        self.__age = None
        self.__marks = None
        
        # Validate age and marks individually
        try:
            self.set_age(age)
        except ValueError as e:
            print(e)
        
        try:
            self.set_marks(marks)
        except ValueError as e:
            print(e)

    def set_name(self, name):
        self._name = name

    def get_name(self):
        return self._name

    def set_age(self, age):
        if age < 5 or age > 100:
            raise ValueError("Age must be between 5 and 100")
        else:
            self.__age = age

    def get_age(self):
        return self.__age

    def set_marks(self, marks):
        if marks < 0 or marks > 100:
            raise ValueError("Marks must be between 0 and 100")
        else:
            self.__marks = marks

    def get_marks(self):
        return self.__marks


name = input("Enter student name: ")
age = int(input("Enter age of the student: "))
marks = int(input("Enter the marks of the student: "))

student = Student(name, age, marks)

print(f"Student Name: {student.get_name()}")
print(f"Student Age: {student.get_age()}")
print(f"Student Marks: {student.get_marks()}")
