# limit = int(input('enter limit'))
# i = 0
# n1 = 1
# n2 = 1
# fibonachi = 0
# print(n1)
# print(n2)
# while i < limit :
#     i = i + 1
#     if i != limit :
#         if i >= 2 :
#             if fibonachi <= limit :
#                  fibonachi = fibonachi + i
#                  print(fibonachi)
#

limit = int(input('enter limit'))
first = 1
second = 1
third = 0
i = 0
fibonachi = [1,1]
while i <= limit :
    i = i + 1
    if i >= 2 :
        third = first + second
        first = second
        second = third
        fibonachi.append(third)
print(fibonachi)