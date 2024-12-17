class User:
    def __init__(self, username):
        self.__username = username 
        self.__password = None  

    def set_password(self, password):
        if len(password) < 8:
            print("Password must be at least 8 characters long.")
            return
        
        contains_digit = False
        contains_special_char = False

        for char in password:
            if char.isdigit():
                contains_digit = True
            if not char.isalnum():  
                contains_special_char = True
        
        if contains_digit and contains_special_char:
            self.__password = password  
            print("Password successfully set.")
        else:
            print("Password must contain at least one number and one special character.")

    
    def check_password(self):
        input_password = input("Enter your password: ") 
        if self.__password == input_password:
            print("Password is correct.")
            return True
        else:
            print("Incorrect password.")
            return False


username = input("Enter your username: ")

user1 = User(username)

password = input("Enter your password: ")
user1.set_password(password) 

user1.check_password()  

