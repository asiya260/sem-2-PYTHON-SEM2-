class Employee:
    def getEmployeeInfo(self):
        self.id=input("Enter ID:")
        self.name=input("Enter the name:")
    def displayEmployeInfo(self):
        print("Id=" , self.id)
    
class Perks(Employee):
    def getDetails(self):
        self.getEmployeeInfo()
        self.sal=int(input("eNTER the salary:"))
    def displayInfo(self):
        self.displayEmployeeInfo()
        print("salary",self.sal)

p=Perks()

p.getEmployeeInfo()
p.getDetails()
p.displayInfo()