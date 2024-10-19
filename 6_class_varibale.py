# class variable ---->class attribute
# circle
# area 
# circum
# in this exercise we will take the diff parameter with same values
# we made a pi variable which is a class variable with this ,we dont need to write the value again again

class Circle:
    pi = 3.14   #1
    def __init__(self,radius):
        self.radius = radius
        

    def calc_circumference(self):
        return 2*Circle.pi*self.radius
    
c = Circle(4)
c1 = Circle(5)
print(c.calc_circumference())

# exercise 2
# in this exercise we give discount for certain period of time 
# with the help of class variable

class Laptop:
    discount = 50
    def __init__(self,brand,model,price):
        self.brand = brand
        self.model = model
        self.price= price
        self.laptop_name = brand + ' ' + model

    def percentage_10(self):
        #   self.price
        off_price =  (Laptop.discount/100)*self.price
        return self.price - off_price

p1 = Laptop('samsung','ax115',65000)
print(p1.percentage_10())

# exercise 3 
# same items with diff discounts
# we use dict method to know the property of laptop
class Laptop:
    discount = 10
    def __init__(self,brand,model,price):
        self.brand = brand
        self.model = model
        self.price= price
        self.laptop_name = brand + ' ' + model

    def percentage_10(self):
        #   self.price
        off_price =  (self.discount/100)*self.price   #1
        return self.price - off_price
# Laptop.discount =0
p1 = Laptop('samsung','ax115',65000)
p2= Laptop('apple','macbook',85000)
p2.discount = 50
print(p1.percentage_10())
print(p1.__dict__)
print(p2.percentage_10())
print(p2.__dict__)

# here we did discount on the p2 for that first we fisrt made a variable p2.discount = 50
# you cant get the 50 % ,to get that discount you have to change the laptop.discount with self.discount in 1
