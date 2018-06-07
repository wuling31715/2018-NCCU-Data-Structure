arr2 = []
total = 0
for i in range(5):
    new = []
    for j in range(5):
        new.append(i + j)
        print(new[j])
    arr2.append(new)
    print('')
for i in range(5):
    for j in range(5):
        total = total + arr2[i][j]
        print('total = %d' % total)        
