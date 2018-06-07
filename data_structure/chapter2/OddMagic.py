# 奇數魔術方陣實作
# File Name: OddMagic.py
# Version

MAX = 15
Square = [[0] * MAX for row in range(MAX)] # 定義矩陣並將矩陣所有元素初始化為0
N = 0 # 矩陣行列大小變數

def anykey_f(): # 按任一鍵即繼續之Function
    try:
        tChar = input('\n\n   Press any key to continue ...')
    except ValueError:
        pass

def init():
    global N
    # 讀取魔術矩陣的大小N，N為奇數且0<=N<=15
    while True:
        N = int(input('\nEnter odd matrix size : '))
        if N % 2 == 0 or N <= 0 or N > 15:
            print('Should be > 0 and < 15 odd number', end = '')
        else:
            break

def Magic():
    global Square
    global N

    Square[0][(N-1)//2] = 1 # 將1放至最上列中間位置
    key = 2
    # i、j記錄目前所在位置
    i = 0
    j = (N - 1) // 2
    while key <= N*N:
        # p、q為下一步位置，i、j各減1代表往西北角移動
        p = (i - 1) % N
        q = (j - 1) % N
        # p < 0（超出方陣上方）則將p移至N-1（最下列）
        if p < 0:
            p = N - 1
        # q < 0（超出方陣左方）則將q移至N-1（最右列）
        if q < 0:
            q = N - 1
        if Square[p][q] != 0: # 判斷下一步是否已有數字
            i = (i + 1) % N # 已有則i往下（填在原值下方）
        else:
            i = p # 將下一步位置assign給目前位置
            j = q
        Square[i][j] = key
        key += 1

def output():
    # 顯示魔術矩陣結果
    print('\nThe %d＊%d Magic Matrix' % (N, N))
    print('------------------------')
    for i in range(N):
        for j in range(N):
            print('%-4d ' % Square[i][j], end = '')
        print()
    anykey_f()

def main(): # 主函數
    init()
    Magic() # 將Square變為 N x N 的魔術矩陣
    output()

main()
