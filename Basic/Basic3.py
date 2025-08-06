

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
#print(floor(2.6))
print(round(2.6))

print(5//2)
print(5**2)
print(6+6)
print("he"+"he")
print(3*3)
print("he"*2)
print(1<2<3<4) #1<2 and 2<3 and......
'''0, 0.0

'' (empty string)

[], {}, set(), None

False 
other than this all are true
'''
print(2 and 6) #6 larger
print(0 and 7) #0
print(2 and "hehe") #str




#f-strings
score=100
height=1.32
is_win=True
print(f"the score is {score} and height is {height}")

#format print
a=10
b="varshi"
print("a is %d b is %s"%(a,b))


