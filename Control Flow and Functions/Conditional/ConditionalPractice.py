print("Welcome to Python pizza deliveries")
size=input("Whats the size of the pizzza? S M L?")
peproni=input("Do you want peproni? Y or N?")
cheese=input("Do you want cheese? Y or N?")
bill=0
if size == "S":
    bill=15
    if peproni=="Y":
        bill+=2
    if cheese=="Y":
        bill+=1
elif size=="M":
    bill=20
    if peproni=="Y":
        bill+=3
    if cheese=="Y":
        bill+=1
else:
    bill=25
    if peproni=="Y":
        bill+=3
    if cheese=="Y":
        bill+=1
print(f"the final bill will ${bill}")