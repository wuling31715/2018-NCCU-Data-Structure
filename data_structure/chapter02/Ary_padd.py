# 多項式相加實作
# 利用陣列表示法做多項式相加
# File Name: Ary_padd.py
# Version

DUMMY = -1

def Padd(a, b, c):
    p = q = r = m = n = 0
    result = ''

    m = a[1]
    n = b[1]
    p = q = r = 2

    while p <= 2*m and q <= 2*n:
        # 比較a與b的指數
        result = compare(a[p], b[q])

        if result == '=':
            c[r+1] = a[p+1] + b[q+1] # 係數相加
            if c[r+1] != 0:
                c[r] = a[p] # 指數assign給c
                r += 2
            # 移至下一個指數位置
            p += 2
            q += 2
        elif result == '>':
            c[r+1] = a[p+1]
            c[r] = a[p]
            p += 2
            r += 2
        elif result == '<':
            c[r+1] = b[q+1]
            c[r] = b[q]
            q += 2
            r += 2

    while p <= 2*m: # 將多項式a的餘項全部移至c
        c[r+1] = a[p+1]
        c[r] = a[p]
        p += 2
        r += 2

    while q <= 2*m: # 將多項式b的餘項全部移至c
        c[r+1] = b[q+1]
        c[r] = b[q]
        q += 2
        r += 2

    c[1] = r // 2 - 1 # 計算c總共有多少非零項

def compare(x, y):
    if x == y:
        return '='
    elif x > y:
        return '>'
    else:
        return '<'

def output_P(p, n):
    i = 0

    print('( ', end = '')
    for i in range(1, n+1):
        print('%d ' % p[i], end = '')
    print(')', end = '')

def main(): # 主函數
    global DUMMY
    # 多項式的表示方式利用只儲存非零項法
    # 分別儲存每一個非零項的指數及個數，
    # 陣列第一元素放多項式非零項個數。
    # ex: 下列A多項式有3個非零項，其多項式為：
    #     5x四次方 + 3x二次方 + 2

    A = []
    B = []

    A.append(DUMMY)
    A.append(3)
    A.append(4)
    A.append(5)
    A.append(2)
    A.append(3)
    A.append(0)
    A.append(2)

    B.append(DUMMY)
    B.append(3)
    B.append(3)
    B.append(6)
    B.append(2)
    B.append(2)
    B.append(0)
    B.append(1)

    C = [0]*12 # 建立陣列C並初始化前12個元素為0

    Padd(A, B, C) # 將A加B放至C

    # 顯示各多項式結果
    print('\nA = ', end = '')
    output_P(A, A[1]*2 + 1) # A[1]*2 + 1為陣列A的大小
    print('\nB = ', end = '')
    output_P(B, B[1]*2 + 1) # B[1]*2 + 1為陣列B的大小
    print('\nC = ', end = '')
    output_P(C, C[1]*2 + 1) # C[1]*2 + 1為陣列C的大小

main()
