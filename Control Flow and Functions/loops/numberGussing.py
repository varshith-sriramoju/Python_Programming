import random as r
'''while True -> looping infinate forever
stops until break
'''
sys=r.randint(0,10)
while True: #infinate loop
    user = int(input("enter a number:"))
    if user<sys:
        print("Number is too small")
    elif user>sys:
        print("Number is too large")
    else:
        print("Congratulations its match")
        break #stop here untill it satify


