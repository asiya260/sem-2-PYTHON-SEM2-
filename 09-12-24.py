class Studentmarks:
    def __init__(self):
        self.Name=input("enter the name of the student:")
        self.English=int(input("enter the mark on english:"))
        self.Math=int(input("enter the mark on Math:"))
        self.Science=int(input("enter the mark on Science:"))
        self.Total=self.English+self.Math+self.Science
        self.percentage=(self.Total/300)*100

    def Display(self):
        print(f"The student named {self.Name} has secured a mark of {self.Total} with a percentage of {self.percentage}")
s=Studentmarks()
s.Display()
        
        
