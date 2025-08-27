#class variable wont need self and
#accessd and modified using class name
class Emp:
    raise_amount=7.5#no self in class variable
    def __init__(self,name,age,sal): #these class varibales only object creation scope
        Emp.raise_amount=7 #class variable  with class name declaration
        self.name=name
        self.age=age
        self.sal=sal
    def increase_sal(self):
        self.sal=self.sal+(self.sal*Emp.raise_amount/100)
    def display(self): #class varibale only when fun called
        Emp.raise_amount=6.2
        print(self.name,self.age,self.sal)
        self.raise_amount#prints
    #raise_amount=6.5

Emp.vari_out='V'#class vari created outside class
print(Emp.vari_out)
a=Emp("varshi",22,40000)
print(a.vari_out)
print("BEFORE")
a.display()
print("AFTER")
a.increase_sal()
a.display()
print(Emp.__dict__)

class Sample:
    i=10
    def init (self):
        self.i=20
s1=Sample()
print(Sample.i) #for class vari as class name
print(s1.i) #for instance vari as object name
