'''while True -> looping infinate forever
stops until break
'''
i=1
total=0
while i<=10:
    print(i)
    total+=i
    i+=1
else:
    print("exe when whole loop got exe")
print("total is:",total)

name=input("enter your name:")
vowels='aeiouAEIOU'
for i in name:
    if i in vowels:
        contains_vowels=True
    else:
        contains_vowels=False
if contains_vowels:
    print("has vowels")
else:
    print("no vowels")

for i in name:
    if i in vowels:
        continue
    print(i)

