# we gonna talk about the instance method(object)  
# l = [2,1,3]
# l.pop()
# here l is instance 
# this pop is a method 

class Person:
    def __init__(self,first_name,last_name,age):
        self.frist_name=first_name
        self.last_name = last_name
        self.age = age

    def full_name(self):
        return f"{self.frist_name} {self.last_name}"
    
    def is_above(self):
     return self.age >18

p1 = Person('mehraj','khan',13)
p2 = Person('sharat','yousuf',23)
print(p1.full_name())       #1
print(Person.full_name(p1)) #2
print(p1.is_above())
print(p2.is_above())

# both are same 1 and 2
# for ex clear method
l = [1,2,3]
l.clear()
print(l)
list.clear(l)
print(l)

# this how the self work in the background
# one more ex 
# def is_above(self):
#     return self.age >18
