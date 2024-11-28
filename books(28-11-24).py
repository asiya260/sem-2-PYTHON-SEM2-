class Books:

    def init(self, name, author):

        self.name = name

        self.author = author



    def show(self):

        print(f"Book Name: {self.name}")

        print(f"Author name: {self.author}")



user=Books("Ram c/o anandhi", "Akhil")

user.show()





class Books:

    

#constructor

    def init(self, name, age=38,publishing =893):

        self.name = name#instance variables

        self.age = age

        self.publishing=publishing



    def show(self):

        print(f"Name={self.name}\nAge={self.age}\nPublishing={self.publishing}")

#object

book=Books("Ram c/o anandhi",40,900)

book.show()





class Books:

    def init(self,name,author):

        self.name="Pride and prejudice"

        self.author="Jane"

    def display(self):

        print(f"Book name={self.name}")

        print(f"Book author={self.author}")

user=Books()

user.display()
