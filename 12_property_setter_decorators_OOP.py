class Phone:
    def __init__(self,brand,model_name,price):    
        self.brand = brand
        self.model = model_name
        self._price = max(price,0)  #1
        # self.complete_sepcification = f"{self.brand} {self.model} and price is {self._price}" #2  #instance variable
    @property
    def complete_specification(self):
           return  f"{self.brand} {self.model} and price is {self._price}" 
    @property
    def price(self):
         return self._price  #5
    @price.setter
    def price(self,new_price):
         self._price = max(new_price,0)
    def make_call(self,phone_number):
        print (f"calling{phone_number}....")    
    def full_name(self):
        return f"{self.brand} {self.model}"    
    
phone1 = Phone('nokia','1100',1000)

print(phone1.brand)
print(phone1.model)
phone1._price = -500
print(phone1.price)   #5
print(phone1.complete_specification) #4

# there are many prblms in that 
# like if we change the price it will chnaged but in 4 it cant change
# to solve this issue make a func rather than instance variable
# if we have negative value and we dont want negative price we can chnage it in 0 value
#         if price >0:
#             self._price = price
#         else:
#             # self._price = 0
# we use this method otherwise look at 1
# @property its a pre-define func if we use this than we dont need to print the 4 as a func 
# means we shouldnot use () in 4 
# we def the func price .hence,we can write price rather than _price
# to make setter func first we have to make decorator than we can make setter
# we use the word that we defined in decorator for ex: @price.stter 