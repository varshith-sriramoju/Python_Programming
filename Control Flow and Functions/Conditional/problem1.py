inp=input("Enter a character:")
if 'a'<=inp<='z':
    print("character is lower case")
elif 'A'<=inp<='Z':
    print("character is upper case")
elif '0'<=inp<='9':
    print("its a number")
else:
    print("a special character")

inp1=input("enter a word")
if bool(inp1.islower()==True):
    print("lower case")
elif bool(inp1.isupper()==True):
    print("upper case")
else:
    print("enter either case only")

