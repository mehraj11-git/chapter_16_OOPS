# can we derive more than one class from base class??
# multilevel inheritance 
# method resolution order 
# method overriding
# isinstance(),issubclass

class Phone:
    def __init__(self,brand,model_name,price):    
        self.brand = brand
        self.model = model_name
        self._price = max(price,0)

    def make_call(self,phone_number):
        print (f"calling{phone_number}....")    
    def full_name(self):
        return f"{self.brand} {self.model}" 


class Smartphone(Phone):
    def __init__(self,brand,model_name,price,internal_memory,ram,rear_camera):   
        super().__init__(brand,model_name,price)
        self.memory = internal_memory
        self.ram = ram
        self.camera = rear_camera

    def full_name(self):
        return f"{self.brand} {self.model} with {self.camera} front camera"  

class Flagshit(Smartphone):
    def __init__(self,brand,model_name,price,internal_memory,ram,rear_camera,front_camera):   
        super().__init__(brand,model_name,price,internal_memory,ram,rear_camera)
        self.front_camera = front_camera


phone1 = Phone('nokia','1100',1000)
andriod1 = Smartphone('smasung','z3',200000,'64 GB','6 GB','20 MP')
andriod2 = Flagshit('oneplus','11pro',300000,'128 GB','16 GB','48 MP','12 MP')
print(phone1.full_name())
print(andriod1.full_name() +  f"and price is {andriod1._price}")
# print(help(Smartphone2))
print(isinstance(andriod1,Smartphone))
print(isinstance(andriod1,Flagshit))
print(issubclass(Smartphone,Phone))
print(issubclass(Smartphone,Flagshit))


# yes we can derive more than one class in base class
# this is what multilevel inheritance works
# method resolution order
# to check the order we use help method 
# method overriding 
# focus on full name func you will get the overriding method
# we overwrite the classess into classess to check the object of the particular class we use 
# isinstance
# note : suppose if i use isinstance to print android1 it shows true for smartphone and for phone
# not for flagshit 
# issubclass
# name itselfs define it 