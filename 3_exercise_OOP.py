# create a laptop class with attributes like brand name,model name ,price 
# create two object /instance of your laptop class

class Laptop:
    def __init__(self,brand_name,model_name,price):
        self.brand = brand_name
        self.model = model_name
        self.price = price
        self.laptop = brand_name + ' '+ price
l1 = Laptop('ASUS','au114tx','£899')
l2= Laptop('SAMSUNG','ax114','£1299')
print(l1.brand)
print(l2.brand)
print(l1.laptop)