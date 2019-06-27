# inp = int(input())
# for i in range(1,n+1) :
#     print(i)

sum = 0
for i in range (1,n+1) :
    sum = float((1 / (i**2)) + sum)
    print(i,sum)