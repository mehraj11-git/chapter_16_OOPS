# make a object and give the discount to the customer 
class Laptop:
    def __init__(self,brand,model,price):
        self.brand = brand
        self.model = model
        self.price= price
        self.laptop_name = brand + ' ' + model

    def percentage_10(self,percent):
        #   self.price
        off_price =  (percent/100)*self.price
        return self.price - off_price




p1 = Laptop('samsung','ax115',65000)
print(p1.percentage_10(30))

# in this exercise first we have make a class 
# and def a func for the discount with two parameter 
# in this we have to first divide the parameter by 100 and than multiply it by self.price
# and store it in a varaible and return the self.price - variable
# and print 