import time
import random
computer_rand = random.randint(1,10)
t_1 = time.time()
while True :
    guessed_number = int(input('enter any number between 1 and 10 = '))
    if guessed_number > computer_rand :
        print('guess less')
    elif guessed_number < computer_rand :
        print('guess more')
    elif guessed_number == computer_rand :
        print('you guessed right !')
        break

t_2 = time.time()
if t_2 - t_1 > 5 :
    print('really ???!!')
# print('time expended = ', t_2 - t_1)