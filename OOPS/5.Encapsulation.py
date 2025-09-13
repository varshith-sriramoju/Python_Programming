#binding of data attributes(variables) and data methods(functions) into single unit
#restict access form outside the class
#about private variables
#__init__()called constructor
#__del__() called destructor
#__ called private
class Emp:
    def __init__(self):
        self.name="varshi"
        self.age=22
        self.__salary=45000 #private variables
    def show(self):
        print(self.__salary)
    def __priMethod(self):
        print()
    def __str__(self):
        return f"Age:{self.age}"
    def __del__(self): #auto executed
        print("successfully destroyed")
a=Emp()
print(a.name,a.age)#no encap as accessing outside the class
#print(a.__salary) cannot access but can by instance/obj methods
a.show() #accessed pri vari through ins/obj method
#a.__priMethod() as pri vari

#but we can accessed it through _****__
print(a._Emp__salary) #this way we can access pri variable
#in pyton ntg is private
print(dir(a))
print(a.__str__())
del a #forcly called destructor but not if obj have more than 1 refer
print("done")
'''
Prevent accidental modification or access from outside the class.
Encapsulate implementation details, making the class interface cleaner.
Signal to other developers that these members are not part of the public API and should not be used directly.
While Python does not enforce strict privacy, using double underscores helps avoid name clashes and accidental access,
supporting better code organization and encapsulation.

'''
