print("welcome to the tip calculator")
bill=float(input("what was the total bill:"))
tip=int(input("how much would you like to tip ? 10 12 or 15?"))
people=int(input("how many people split:"))
tip_percent=(tip/100) #12%=12/100
tip_amount=tip_percent*bill #how much 12
tip_and_bill=tip_amount+bill #add tip to bill
split=round(tip_and_bill/people,2) #split
print(f"each person to pay {split}")

