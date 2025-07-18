from numpy.ma.core import floor

print("my age is "+str(21))
#TypeError: can only concatenate str (not "int") to str
#to add DIRECT numbers to print statement type convert to str
print(12+12)
print(12-12)
print(12*12)
print(12/13) #float type
print(12//13)#int type
print(2**2) #2 square
print(2**3) #2 cube
'''PEMDAS
p ()
e **
m *
d /
a +
s -
'''
print(3*(3+3)/3-3) #3
print(3*3+3/3-3) #7

height = 1.65
weight = 84
bmi=float(weight)/height**2
print(bmi)
print(round(bmi)) #nearest round number
print(round(bmi,2))
print("-----------------")
print(floor(2.6))
print(round(2.6))

#f-strings
score=100
height=1.32
is_win=True
print(f"the score is {score} and height is {height}")


