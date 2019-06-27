import random
computer_rand = random.random(1,10)
while true :
    guessed_number = int(input('enter any number'))
    if guessed_number == computer_rand :
        print('you guessed right')
        break

print('end')