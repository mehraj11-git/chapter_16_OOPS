# inhereitance method 
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
        # Phone. __init__(self,brand,model_name,price)  #uncommon way
        super().__init__(brand,model_name,price)
        self.memory = internal_memory
        self.ram = ram
        self.camera = rear_camera

    # def make_call(self,phone_number):
    #     print (f"calling{phone_number}....")    
    # def full_name(self):
    #     return f"{self.brand} {self.model}" 

phone1 = Phone('nokia','1100',1000)
Smartphone1 = Smartphone('smasung','z3',200000,'64 GB','6 GB','20 MP')
print(phone1.full_name())
print(Smartphone1.full_name() +  f"and price is {Smartphone1._price}")

# here made a lengthy code to print detials of the both phones
# for inheritance mehtod we can make it small code
# we made a code for phone than why do we make another lengthy code ?? 
# to make it short we do inheritate the class phone into smartphone class