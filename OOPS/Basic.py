class Sample:
    pass
x=Sample()
print(type(x))#__main__.Sample
print(x) #obj address

class Emp:
    def __init__(self):
        print("obj created")
x=