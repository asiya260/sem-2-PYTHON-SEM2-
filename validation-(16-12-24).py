class Product:
    def __init__(self, name, price, stock):
        
        self.__name = name
        self.__price = None  
        self.__stock = None  
        
        self.set_price(price)
        self.set_stock(stock)
        
    def set_price(self, price):
        if price <= 0:
            print("Price must be greater than 0.")
        else:
            self.__price = price
            print(f"Price set to {self.__price}")
    
    
    def set_stock(self, stock):
        if isinstance(stock, int) and stock >= 0:
            self.__stock = stock
            print(f"Stock set to {self.__stock}")
        else:
            print("Stock must be a non-negative integer.")
    
    def get_stock(self):
        return self.__stock

name = input("Enter your product name: ")
price = float(input("Enter product price: ")) 
stock = int(input("Enter your stock: "))  


product1 = Product(name, price, stock)

print(f"Product stock is: {product1.get_stock()}")
