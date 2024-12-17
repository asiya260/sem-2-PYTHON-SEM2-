class Student:
    def dias(self):
        self.name=name
        self.age=age
    def get_name(self):
        return self.name
    def get_age(self):
        return self.age
    def set_name(self,name):
        self.name=name
    def set_age(self,age):
        self.age=age
        
name=input("enter the name:")
age=int(input("enter the age:"))
s=Student()
n=input()
s.set_name(n)
print(f"name:{s.get_name()} \n Age={s.get_age()}")

