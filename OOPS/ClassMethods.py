#instance methods self parameter
#class method cls parameter
#cls and self are called reference objects
class ClassMethod:
    @classmethod #decorator
    def sample(cls): #cls parameter
        pass
class Emp:
    raise_amount=0 #class variable
    def __init__(self,name,age,sal):
        self.name=name
        self.age=age
        self.sal=sal
    def increse_sal(self):
        self.sal=self.sal+(self.sal*Emp.raise_amount/100)
    def display(self):
        print(f"name:{self.name} age:{self.age} sal:{self.sal}")
inp=int(input("Enter raise percentenage:"))
Emp.raise_amount=inp
print("Before Incrementing")
e1=Emp('Varshi',22,45000)
e1.display()
print("After incrementing")
e1.increse_sal()
e1.display()
