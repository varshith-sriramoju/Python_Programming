import math
#instance methods
#instance variables self,a,b,c... as they change for every object/instance
class Sample:
    def __init__(self,a,b,c): #instance variables
        self.a=a #if no parameters then they are local vari
        self.b=b
        self.c=c
    def instance_method(self): #instance method
        print(f"a:{self.a} b:{self.b} c:{self.c}")
a=Sample(1,2,3)
a.instance_method()
print("------------------------------------------------------")
class Circle:
    def __init__(self,radius):
        self.radius=radius
    def cal_area(self):
        area=math.pi*math.pow(self.radius,2) #local variable
        print(f"area of circle is {area}")
    def cal_circum(self):
        print(f"circumference of circle is {2*3.14*self.radius}")
    def randomInstance(self,p):
        self.p=p
    def delRandomInstance(self):
        del self.p
b=Circle(10)
b.cal_area()
b.cal_circum()
#__dict__
print(b.__dict__) #gives us instance variables in dict form
b.__dict__['sample']=1
b.randomInstance("q")
print(b.__dict__) # this will print all instances variables of the class
b.delRandomInstance() #del the instance selected
print(b.__dict__) #updated
del b
try:
    print(b.__dict__) #deleteing coompletely
except:
    print("not defined")
