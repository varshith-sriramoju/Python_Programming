#instance methods
#instance variables self,a,b,c... as they change for every object/instance
class Sample:
    def __init__(self,a,b,c): #instance variables
        self.a=a
        self.b=b
        self.c=c
    def instance_method(self): #instance method
        print(f"a:{self.a} b:{self.b} c:{self.c}")
a=Sample(1,2,3)
a.instance_method()
print("------------------------------------------------------"
