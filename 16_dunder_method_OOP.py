# special majic method or dunder method
# if the func  start with double _  and end with double _ than its call dunder method or special mathod 
# for ex: __init__,__name__,__dict__ etc...
# operator overloading
# polymorphism
class Phone:
    def __init__(self,brand,model_name,price):    
        self.brand = brand
        self.model = model_name
        self._price = max(price,0)
    def full_name(self):
        return f"{self.brand} {self.model}" 
    def __str__(self):
        return f"{self.brand} {self.model}"
    def __repr__(self):
         return f"{self.brand} {self.model} and the price is {self._price}"
    def __len__(self):
        return len(self.full_name())
    def __add__(self,other):
        return self._price + other._price   
# 2+3 = 5  #2
# abs +scs = absscs
l = [1,2,3] #1
# print(l)
# print(len(l))
my_phone = Phone('nokia','1100',1000)
my_phone2 = Phone('nokia','1100',1000)
print(my_phone+my_phone2)
# print(str(my_phone))
# print(repr(my_phone))
# print(len(my_phone))

# at 1 the values of l is print
# whereas the value of my_phone donot print rather it shows the location
# to solve that issue we use dunder method
# we can do this str or repr method
# we can directly use the len func to print the length of the list, string, tuple etc..
# but we have to def a func to get the length of the object
# overloading:-
# if you have to add two objects we have to define a add fun 
# we take two parameter first will be the self and the other one
# polymorphism :-
# overriding --->polymorphism