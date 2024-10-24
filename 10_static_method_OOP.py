# static method ----> normal func 
# we cant use normal func in class it will raise error
# to avoid such errors we use the static method 
# it is similar to the class method it means that 
# it is created by decorators but in static method 
# we donot call the parameters like --->  cls,self
# lets try 

class Person:
    count = 0
    def __init__(self,first_name,last_name,age):
        Person.count +=1
        self.first = first_name
        self.last = last_name
        self.age = age
    @staticmethod
    def hello():
        return f"{'hello world'}"
    @classmethod
    def names(cls,string):
        first,last,age = string.split(',')
        return cls(first,last,age)
    @classmethod
    def counnt_instance(cls):
        return f"you have created {cls.count} instances of {cls.__name__} "
    def full_name(self):
        return f"{self.first} {self.last}"
    def is_above(self):
        return self.age>18
p1 = Person.names('mehraj,khan,24')    
print(p1.full_name())
print(p1.hello())