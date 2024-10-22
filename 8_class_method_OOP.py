# class method 
# diff btw class method and class intance /

class Person :
    age = 24
    count_instance = 0
    def __init__(self,first_name,last_name):
        Person.count_instance +=1
        self.first = first_name
        self.last = last_name
        

    @classmethod
    def count_instances(cls):
        return f"you have created {cls.count_instance} instances of {cls.__name__} class"
    
    def full_name(self):
        return f"{self.first} {self.last}"
    
    def is_above(self):
        return self.age >18
p1 = Person('merhaj','khan')
p2 = Person('mohammed','syed')
print(Person.count_instances())

# in this exercise we set the age as a class variable
# than  take another class variable whose initial value is zero 
# aftr def the init we increase the value of the class variable 
# we difine the class method with the help of decorator
# with this method we got to know how many objects we created
