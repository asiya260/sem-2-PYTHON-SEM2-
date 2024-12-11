class College:
    def __init__(self, CollegeName, Location):
        self.CollegeName = CollegeName
        self.Location = Location

    def displaycollege_info(self):
        print("College Name:", self.CollegeName, "Location:", self.Location)

class Employee(College):
    def __init__(self, CollegeName, Location, nameep, job):
        super().__init__(CollegeName, Location)  # Correctly calling the parent constructor
        self.nameep = nameep
        self.job = job

    def displaycollege_info(self):
        print("Employee:", self.nameep, "Job is:", self.job)

class Salary(College):
    def __init__(self, CollegeName, Location, salary):
        super().__init__(CollegeName, Location)  # Correctly calling the parent constructor
        self.salary = salary

    def salary_info(self):
        print("Employee Salary:", self.salary)

class Display(Employee, Salary):
    def __init__(self, CollegeName, Location, nameep, job, salary):
        Employee.__init__(self, CollegeName, Location, nameep, job)  # Calling Employee's constructor
        Salary.__init__(self, CollegeName, Location, salary)  # Calling Salary's constructor

# Taking inputs from the user
CollegeName = input("Enter College Name: ")
Location = input("Enter College Location: ")
nameep = input("Enter Employee Name: ")
job = input("Enter Employee Job: ")
salary = int(input("Enter Employee Salary: "))

# Creating an instance of the Display class
display_obj = Display(CollegeName, Location, nameep, job, salary)

# Displaying information
display_obj.displaycollege_info()  # This will display employee info
display_obj.salary_info()  # This will display salary info
