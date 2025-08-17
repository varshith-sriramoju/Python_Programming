while True:
    num=int(input("enter a number:"))
    if num==0:
        break
    else:
        for i in range(1,num+1):
            print(i)
print("-------OR--------")
x=int(input("enter a number:"))
while x!=0:
    for i in range(1,x+1):
        print(i)
    x=int(input("enter a number:"))

