# in this we have to check the how many intence we have 
# for that we have to make a variable with 0 and then increase it 
class Person :
    age = 24
    counted_instance = 0
    def __init__(self,first_name,last_name):
         Person.counted_instance += 1
         self.first = first_name
         self.last = last_name
    def ages(self):
         return self.age     
   
name = Person('mehraj','khan')
names = Person('sharat','yousuf')
names.age = 23
print(name.counted_instance)
print(names.age)
print(name.age)