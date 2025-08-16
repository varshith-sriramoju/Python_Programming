for i in range(1,5):
    print("***")

for i in range(1,5):
    for j in range(1,i+1):
        print("*",end='')
    print()#new line
print("--------------------------")
for i in range(1,5):
    for j in range(i,5):
        print("*",end='')
    print()
print("-----OR------")
for i in range(4,0,-1):
    for j in range(1,i+1):
        print("*",end="")
    print()
print("---------------------")
star=int(input("enter number of stars:"))
for i in range(1,star+1):
    for j in range(1,i+1):
        print("*",end='')
    print()
for i in range(1,star+1):
    for j in range(i,star+1):
        print("*",end='')
    print()
