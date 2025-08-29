def add(a,b):
    c=a+b
    print(f"{a}+{b}:{c}")
add(1,2)

def ret(a,b):
    c=a*b
    return c #just returns but wont print
print(ret(22,2))
x=ret(2,2)

print(x)
def abs(n):
    if n>0:
        return n
    else:
        return -n #-*-=+
print(abs(-9)) #9

def factorial(n):
    f=1
    while n>1:
        f=f*n
        n=n-1
    return f
print(factorial(5))

def greet(name):
    print("Hello ",name)
    return name
x=greet("varshi")
print(x) #if return ok if not none

#multiple return values
def cal(a,b):
    c=a+b
    d=a-b
    return c,d
x,y=cal(5,3)
print("Sum is",x,"Difference is",y)
z=cal(2,1) # automatically tuple
print(z)
print("sum is ",z[0],"diff is ",z[1])

#scope of varibale
r=1
def sth0():
    print(r)
sth0()
def sth():
    global r
    r=7
    print(r)
sth()
def sth1():
    r=3
    print(r)
sth1()

def foo(x,y):
    global a
    a=12
    b=45
    x,y=y,x
    b=13
    c=10
    print(a,b,x,y)
a,b,x,y=78,14,18,19
foo(23,22)
print(a,b,x,y)