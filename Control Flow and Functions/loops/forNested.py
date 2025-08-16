num=[1,2,3]
alpha=['a','b','c']
for i in num:
    print(i)
    for j in alpha:
        print(j)
print("2 table upto 10times")
for i in range(2,3):
    for j in range(1,11):
        print(f"{i} * {j} = {i*j}")
else:
    print("The about table executed succesfully")