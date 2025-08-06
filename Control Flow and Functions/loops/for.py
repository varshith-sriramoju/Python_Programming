from Basic.Basic3 import score

#range function
for i in range(1,10,2):
    print(i) # 1 3 5 7 9

fruits=["apple","peach","pear"]
for i in fruits:
    print(i)
    print(i+" pie")

marks=[1,2,3,4,5,6,7,8,9,11]
sum=0
for i in marks:
    sum+=i
print(sum)

max=0
for i in marks:
    if i>max:
        max=i
print(max)

#sum=0
for i in range(1,101):
    sum+=i
print(sum)

for i in range(1, 101):
    if i % 3 == 0 and i % 5 == 0:
        print("FizzBuzz")
    elif i % 3 == 0:
        print("Fizz")
    elif i % 5 == 0:
        print("Buzz")

    else:
        print(i)

