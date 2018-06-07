N = 3 
arr_a = [[0] * N for row in range(N)]
arr_b = [[0] * N for row in range(N)]
arr_c = [[0] * N for row in range(N)]


for i in range(N):
    for j in range(N):
         arr_a[i][j] = N
         arr_b[i][j] = N 

for row in arr_a:
    print(row)

for i in range(N):
    for j in range(N):
        for k in range(N):
            arr_c[i][j] = arr_c[i][j] + (arr_a[i][j] * arr_b[j][i])

for row in arr_c:
    print(row)


