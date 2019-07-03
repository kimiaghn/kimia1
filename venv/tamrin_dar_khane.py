# from random import randint as rand_number
# import time
# computer_num = rand_number(1,10)
# time_before = time.time()
# while True :
#     guesses_num = int ( input ( 'enter a number' ) )
#     if guesses_num > computer_num :
#         print('try less')
#     elif guesses_num < computer_num :
#         print('try more')
#     elif guesses_num == computer_num:
#         print('horray')
#         break
# time_after = time.time()
# print(time_before, time_after)

for i in range(1,256) :
    if (i >=65 and i <= 90) or (i >=97 and i <=122):
        print(chr(i) , i)