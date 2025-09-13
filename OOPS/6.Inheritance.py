#inheritance builds reusability
#5 types
#single inheri
class Animal:
    def eat(self):
        print("it eats")
    def sleep(self):
        print("it sleeps")
class Bird(Animal):
    def set_type(self,type):
        self.type=type
    def fly(self):
        print("it flyes")
    def __str__(self):
        return f"this is a {self.type}"
duck=Bird()
duck.set_type("duck")
#__str__ accessed through print() argu to obj name
print(duck)
print(duck.__str__())
duck.sleep()

#if child has no init then calls parent init
#if has calls child init
class A:
    def __init__(self):
        print("inti of A")
class B(A):
    pass
obj=B() #calls A init

#but how to call parent class instance to child
#either using name of class explicity or super():calls parent methods
class Rectangle:
    def __init__(self):
        self.len=10
        self.brt=5
class Cuboid(Rectangle):
    def __init__(self):
        super().__init__()
        #Rectangle.__init__(self)
        self.hei=2
    def volume(self):
        print(self.len*self.brt*self.hei)
obj=Cuboid()
obj.volume()
'''
 The answer is that super( ) gives 4 benefits:
  We don’t haveto pass self whilecalling any method using super().
  If the nameof parentclass changesafterinheritance then wewillnot
 have to rewritethe code in child as super() will automatically connect
 itself to current parent
  Itcanbe usedto resolve methodoverriding
  Itis veryhelpful in multiple inheritance

'''
#if child has no init then calls parent init
#if has calls child init
#method overriding called redefine method with same name
#Thus, MethodOverridingis aconcept in OOPwhich
# occurs whenever a derived(child) class redefines the same
# methodas inheritedfrom the baseclass(parent)

class Person:
    def __init__(self,age,name):
        print("Parent")
        self.age=age
        self.name=name
class Emp(Person):
    def __init__(self,age):
        super().__init__(age) #match with child
        print("child")
        print(self.name)

c=Emp(21)
print(c)
p=Person(21,"varshi")
print(p)