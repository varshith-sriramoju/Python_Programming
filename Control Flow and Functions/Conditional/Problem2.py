a=int(input("enter 1 integer"))
b=int(input("enter 2 integer"))
c=int(input("enter 3 integer"))
if a>b:
    if a>c:
        print(f"{a} is greater")
    else:
        print(f"{c} is greater")
elif b>a:
    if b>c:
        print(f"{b} is greater")
    else:
        print(f"{c} is greater")
else:
    print("all were equal")

year=int(input("Enter a year:"))
if (year%4==0 and year%100!=0) or year%400==0 :
    print("a leap year")
else:
    print("not a leap year")

