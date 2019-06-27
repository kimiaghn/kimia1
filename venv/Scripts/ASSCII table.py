# for i in range (0,255) :
#   print( *[i, chr(i)])


columns = 8
rows = 256 // columns
for i in range(rows) :
    for j in range(2) :
        num = i * columns + j
        print(num , chr(num), end = '\t|\t')
    print()