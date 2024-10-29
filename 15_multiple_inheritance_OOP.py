class A :
    def class_a_method(self):
        return 'I\'m just a class A method' 
    def hello(self):
        return 'hello from class A'
class B :
    def class_b_method(self):
        return 'I\'m just a class B method' 
    def hello(self):
        return 'hello from class B'
    
class C(A,B):   #1
    pass

instance_c= C()
print(instance_c.class_a_method())
print(instance_c.class_b_method())
print(instance_c.hello)
# print(help(instance_c))
print(C.mro())
print(C.__mro__)

# here if we wanna print about the hello func 
# this will print the first hello method means class A Not the class B
# if we want to print the class B hello func we have to change the order in 1