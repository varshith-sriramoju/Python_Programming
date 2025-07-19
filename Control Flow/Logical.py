weight = 85
height = 1.85
# and both true
# or any one true
# not true becomes false
bmi = weight / (height ** 2)
if bmi <18.5:
    print("underweight")
elif bmi >=18.5 and bmi<24.9:
    print("normal weight")
else:
    print("overweight")