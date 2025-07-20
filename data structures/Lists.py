import random
states_of_india=["Tg","Ap","Ka","TN"]
print("old:"+states_of_india[0])
print(states_of_india[-1])
states_of_india[0]="TG"
print("new:"+states_of_india[0])
states_of_india.append("KL") #add at last
print(states_of_india)

friends=["hopper","el","otis","maeve"]
print(random.choice(friends))
#or
ran_int=random.randint(0,3)
print(friends[ran_int])

a=[1,2,3]
b=[4,5,6]
c=[a,b]
print(c) #[[1, 2, 3], [4, 5, 6]]
print(c[0][0]) #1
print(c[1][1]) #5