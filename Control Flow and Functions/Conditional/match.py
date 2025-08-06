#py 3.9 doesnot support match
day=1
match day:
    case 0:
        print("one")
    case 2:
        print("two")
    case _:
        print("Else statement")