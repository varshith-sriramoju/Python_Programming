#subscripting
from Basic.Basic1 import length

print("Hola"[0])

print("Hola"[-1])
print("123"+"123")
print(123+123)
print(1.2+1.2)
print(type(123))
print(type(1.2))#<class 'float'>
#DT conversion
print(int("100")+int("100"))

#String cannot convert to integer but reverse possible
#print(int("abc")+int("123")) value error

'''a=int("asd") valueerror as asd cannot be converted into int 
print(a)'''
b=str(123)
print(b)
c=int("123") #no error as "123" can be easily convertable
print(c)

name=input("enter your name:")
length=len(name)
print("total numbers in your name:"+str(length))
