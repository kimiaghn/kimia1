# for i in range (0,255) :
#   print( *[i, chr(i)])


columns = 8
rows = 256 // columns
for i in range(rows) :
    for j in range(2) :
        num = j * 2 + i
        print(num , chr(num), end = '\t|\t')
    print()