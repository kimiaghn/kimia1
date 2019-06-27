# inp = int(input())
# for i in range(1,n+1) :
#     print(i)

sum = 0
n = int(input('enter n'))
for i in range (1,n+1) :
        sum = (1 / (i**2)) + sum
    print(i,sum)
print((sum * 6)**0.5)
