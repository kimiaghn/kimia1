mass = int(input("enter mass"))
height = int(input("height"))

bmi = float(mass / ( height ** 2))


if bmi <= 18 :
    print('under weight')
elif 18 < bmi <=25 :
    print('normal')
elif 25 < bmi <= 30 :
    print('over weight')
else :
    print("obesety")

