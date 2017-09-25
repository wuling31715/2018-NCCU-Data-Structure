def main(N):

    triangle = [[0] * (i + 1) for i in range(N)]

    for i, row in zip (range(len(triangle)), triangle):
        for j in range(len(row)):
            if j == 0 or j == (len(row) - 1):
                triangle[i][j] = 1
            else:
                triangle[i][j] = triangle[i - 1][j - 1] + triangle[i - 1][j]

    for i, row in zip (range(len(triangle) + 1), triangle):
        print(' ' * int((len(triangle) - i)), end = '')
        for j in row:
            print(j, end = ' ')
        print()

N = input('Please input the degree: ')        
N = int(N)
main(N) 
