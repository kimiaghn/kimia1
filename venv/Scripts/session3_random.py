import random
computer_random = random.random()
while true :
    guessed_number = int(input('enter any number'))
    if guessed_number == computer_random :
        print('you guessed right')
        break
