# OBJECTIVES
# WHAT IS class 
# HOW TO CREATE A CLASS
# WHAT IS INIT METHOD (constructor)
# WHAT ARE ATTRIBUTES,INSTANCE VARIABLE
# HOW TO CREATE OUR OBJECT

# CLASS IS BLUE PRINT WE WILL DECIDE WHAT WILL COME IN OUR CODE 
class Person:
    def __init__(self,first_name,last_name,age):
        # instanace variables
        print('init method get called')
        self.fisrt_name = first_name
        self.last_name = last_name
        self.age = age

p1 = Person('mehraj','khan',23)
p2 = Person('khaled','yousuf',27)
print(p1.fisrt_name)
print(p2.fisrt_name)





# first letter of your class name should be in caps
# we create class to make our objects(p1 and p2 ect)
# we can make enough objects 
# we can write any name instead of self 
# self.fisrt_name <----self.anyname_fisrt_name we can give any name here the main func occur
#  by the parameters that we call in def func
# first_name,last_name,age ----> we call them as attribute