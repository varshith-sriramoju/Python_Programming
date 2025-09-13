#instance methods self parameter
#class method cls parameter with decorator
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

class Person:
    count = 0
    def __init__(self, name):
        self.name = name
        Person.count += 1
    @classmethod #common for all objs created form the class irres of objs
    def get_count(cls):
        print("Called from", cls)
        return cls.count
# Usage
p1 = Person("Alice")
p2 = Person("Bob")
print(Person.get_count())
#class methods produce similar output whereas instance methods may
#change output from obj to obj
