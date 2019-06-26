mass = int(input("enter mass"))
height = int(input("height"))
if height > 10:
     height = height / 100


bmi = float(mass / ( height ** 2))


if bmi < 18 :
    print('under weight')
elif bmi <= 25 :
    print('normal')
elif bmi <= 30 :
    print('over weight')
else :
    print("obesety")

