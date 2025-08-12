inp=int(input("enter a number:"))
a=0
for i in range(1,inp+1):
    a+=i
print(f"sum of 1 to {inp}:",a)
fact=1
for i in range(1,inp+1):
    fact*=i
print(f"factorial of {inp}:",fact)
