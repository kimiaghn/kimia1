# inp = int(input())
# for i in range(1,n+1) :
#     print(i)

# sum_r = 0
# n = int(input('enter n'))
# for i in range (1,n+1) :
#         sum_r = (1 / (i**2)) + sum_r
#     print(i,sum_r)
# print('pi =')
# print((sum_r * 6)**0.5)

n = 1000
zeta = 0
i = 1
while 3.1415 - zeta > 0.0001 :
    zeta = zeta + (1 / i**2)
    i = i + 1
print(zeta)