def main(N):

    trangle = [[0] * (i + 1) for i in range(N)]

    for i, row in zip (range(len(trangle)), trangle):
        for j in range(len(row)):
            if j == 0 or j == (len(row) - 1):
                trangle[i][j] = 1
            else:
                trangle[i][j] = trangle[i - 1][j - 1] + trangle[i - 1][j]
            #print(trangle[i][j])    

    for i, row in zip (range(len(trangle) + 1), trangle):
        print(' ' * int((len(trangle) - i)), end = '')
        for j in row:
            print(j, end = ' ')
        print()


N = input('Please input the degree:\n')        
N = int(N)
main(N)        
