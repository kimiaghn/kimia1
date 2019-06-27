import time
import random
computer_rand = random.randint(1,10)
t_1 = time.time()
while True :
    guessed_number = int(input('enter any number = '))
    if guessed_number == computer_rand :
        print('you guessed right !')
        break

t_2 = time.time()
print('time expended = ', t_2 - t_1)