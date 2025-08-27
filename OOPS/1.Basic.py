#NO method/function Overloading
#Sol is Default arguments
class Sample:
    pass
x=Sample()
print(type(x))#__main__.Sample
print(x) #obj address
print("-----------------------------------------------------")
class Emp:
    def __init__(self): #we can give any 1 foraml argumnet but prefer self
        print("obj created")
y=Emp() #fun
z=Emp() #fun
a=Emp() #fun
print(y) #obj address
print("-----------------------------------------------------")
class STudent:
    def __init__(self,age=1,name="V",college="vaag"):
        self.age=age #instance or object variables
        self.name=name
        self.college=college
v=STudent(age=22,college="VGSE",name="varshi") #referance varibales
print(v) #returns only obj address
v.name="Varshith" #to change
print(f"age:{v.age}")
print(f"name:{v.name}")
print(f"college:{v.college}")
print("-----------------------------------------------------")
#new object creation
a=STudent() #default values consideration
print(f"age:{a.age}")
print(f"name:{a.name}")
print(f"college:{a.college}")
print("-----------------------------------------------------")
#new values
b=STudent(1,"varsh","VAAG")
print(f"age:{b.age}")
print(f"name:{b.name}")
print(f"college:{b.college}")
