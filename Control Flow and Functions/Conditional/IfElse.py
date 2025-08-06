age=22
msg="Kid"if age<=18 else "Adult"
print(msg)

print("welcome to rollarcoster")
height=int(input("whats ur height in cm:")) #assignment =
bill=0
if height>=120:
    print("you can")
    age=int(input("enter your age:"))
    if age<18:
        bill=100
        print("please pay ₹100")
    elif age==18: #checking equality
        bill=150
        print("please pay ₹150")
    elif age==19:
        bill=180
        print("please pay ₹180")
    else:
        bill=200
        print("please pay ₹200")
    want_photo=input("if you want photo? \"yes\" or \"no\":")
    if want_photo == "yes":#50 extra for photo
        bill+=50
    # else: no use of writing
    #     bill==bill
    print(f"your final bill is ₹{bill}")


else:
    print("no you can't")