#always postional arguments first then later other
# Positional Argument
def add(a,b):
    print(a+b)
add(1,1)
# Keyword Argument
def suum(a,b):
    print(a+b)
suum(a=1,b=1)
# Default Argument
def fullName(fname,lname="Sriramoju"): #paste def values last
    print(f"hello {fname} {lname}")
fullName("varshith") #def
fullName("varsh","sri")
# Variable Length Argument
def findLargest(*names): #infinate arguments but only 1 parameter
    lar=''
    max=0
    for i in names:
        if len(i)>max:
            max=len(i)
            lar=i
    return lar
print(findLargest("hi","hiiiiiiii","helloo"))
