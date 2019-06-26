
n = int(input('enter number'))
i = 0
factoriel = 1
# n = 4
while i < n :
    i = i+ 1
    if i != n :
        factoriel = factoriel * (i+1)
        print(i)
        print(factoriel)
print(factoriel)