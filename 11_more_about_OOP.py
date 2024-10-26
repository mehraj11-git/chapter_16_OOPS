# encapsulation:-

# Encapsulation in Python means keeping the details of an object's data and methods hidden, 
# so you can control how they're accessed and modified, making your code safer and easier to manage.

# abstraction :-

# Abstraction in Python is the concept of hiding complex implementation details and showing
# only the essential features of an object or system. 
# It allows you to focus on what an object does rather than how it does it,
# making your code simpler and more focused on the relevant details.

# some special naming convention
# __name__ ,__dict__ ----->dunder,magic method

# name mangling



class Phone:
    def __init__(self,brand,model_name,price):    
        self.brand = brand
        self.model = model_name
        self._price = price
    def make_call(self,phone_number):
        print (f"calling{phone_number}....")    
    def full_name(self):
        return f"{self.brand} {self.model}"    
    
phone1 = Phone('nokia','1100',1000)
# print(phone1._price)
# phone1._price = -1000
print(phone1._price)
print(phone1.__dict__)

l = [3,4,6,2,1]
l.sort()
print(l)

# there are lot of algorithm use in sort method we donot know
# quick sort
# merge sort
# tim sort 