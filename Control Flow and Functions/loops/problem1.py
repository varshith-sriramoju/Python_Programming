a=0
while True:
    inp = int(input("Enter an interger(press 0 to stop):"))
    if inp!=0:
        if inp<=-1: #-1 is bigest and int<=-1 means -1 to -infinate
            continue
        a+=inp
    else:
        print(f"sum is {a}")
        break
'''while true means infinate loop 
can be exicted by only by break
'''
