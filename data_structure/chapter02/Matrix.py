# 矩陣相乘實作
# 將兩矩陣行列相乘之和放入第三個矩陣
# File Name: Matrix.py
# Version

N = 5
C = [[0] * N for row in range(N)]

def access_matrix(A, B):
    global C
    
    # 將A矩陣每一列元素與B矩陣每一列元素
    # 相乘之和放入C矩陣之中
    for i in range(N):
        for j in range(N):
            sum = 0
            for k in range(N):
                sum += A[i][k] * B[k][j]
            C[i][j] = sum

def output_result(A, B):
    global C
    # 列出三矩陣內容
    print("\nContent of Matrix A :\n")
    output_Matrix(A)
    print("\nContent of Matrix B :\n")
    output_Matrix(B)
    print("\nContent of Matrix C :\n")
    output_Matrix(C)

def output_Matrix(m): # 輸出陣列內容
    for i in range(N):
        for j in range(N):
            print(" ", m[i][j], end = '')
        print() # 輸出完一列跳行

def main(): # 主函數
    global N

    A = [[0]*N for row in range(N)] # 宣告5x5陣列A並將所有元素指定為0
    B = [[0]*N for row in range(N)] # 宣告5x5陣列B並將所有元素指定為0

    for i in range(N):
        for j in range(N):
            A[i][j] = j + 1 # 給5x5的陣列A指定初始值
    for i in range(N):
        for j in range(N):
            B[i][j] = -(j - 5) # 給5x5的陣列B指定初始值

    access_matrix(A, B)
    output_result(A, B)

main()
