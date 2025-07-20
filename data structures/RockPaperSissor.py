import random

print("what do you choose")
inp=int(input("type 0 for rock 1 for paper 2 for sissor:"))
if inp==0:
    print("you choosed rock")
elif inp==1:
    print("you choosed paper")
else:
    print("you choosed sissor")

options=["rock","paper","sissor"]
random_int_by_computer=random.randint(0,2)
if random_int_by_computer==0:
    print("computer choosed 0 rock")
    if inp==0: #rock
        print("tie")
    elif inp==1: #paper
        print("you win")
    else: #sissor
        print("you lose")
elif random_int_by_computer==1:
    print("computer choosed 1 paper")
    if inp==0: #rock
        print("you lose")
    elif inp==1: #paper
        print("tie")
    else:
        print("you win") #sissor
else: #sissor
    print("computer choosed 2 sissor")
    if inp==0: #rock
        print("you win")
    elif inp==1: #paper
        print("you lose")
    else:
        print("tie") #sissor

