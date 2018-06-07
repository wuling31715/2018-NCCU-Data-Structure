# 利用Dijkstra演算法求最短路徑
# File Name: G_shpath.py
# Version

import sys

MAX_V = 100
VISITED = 1
NOTVISITED = 0
Infinite = 1073741823

# A[1..N][1..N]為圖形的相鄰矩陣
# D[i] 1..N 用來儲存某起始頂點到i節點的最短路徑
# S[1..N] 用來記錄頂點是否已經拜訪過
# P[1..N] 用來記錄最近經過的中間節點
A = [[0] * (MAX_V+1) for row in range(MAX_V+1)]
D = [0] * (MAX_V+1)
S = [0] * (MAX_V+1)
P = [0] * (MAX_V+1)

source = 0
sink = 0
N = 0
step = 1
top = -1 # 堆疊指標

Stack = [0] * (MAX_V+1) # 堆疊空間

def init():
    global A
    global S
    global D
    global P
    global Infinite
    global N
    global NOTVISITED
    global VISITED
    global source
    global sink

    weight = 0
    done = False

    try:
        inputStream = open('sh_path.dat', 'r')
    except FileNotFoundError:
        print('File sh_path.dat not found!')
        sys.exit(1)

    # 讀取圖形節點數
    try:
        N = eval(inputStream.readline().strip('\n'))
    except Exception:
        pass

    for i in range(1, N+1):
        for j in range(1, N+1):
            A[i][j] = Infinite # 起始A[1..N][1..N]相鄰矩陣

    while done == False:
        try:
            temp = inputStream.readline().strip('\n').split(' ')
            i = eval(temp[0])
            j = eval(temp[1])
            weight = eval(temp[2])
        except Exception:
            done = True
        A[i][j] = weight # 讀取i節點到j節點的距離weight

    inputStream.close()

    source = eval(input('Enter source node: '))
    sink = eval(input('Enter sink node: '))

    # 起始各陣列初始值
    for i in range(1, N+1):
        # 各頂點設為尚未拜訪記錄起始頂點至各頂點最短距離
        S[i] = NOTVISITED
        D[i] = A[source][i]
        P[i] = source

    # 起始節點設為已經走訪
    S[source] = VISITED
    D[source] = 0

def access():
    global step
    global A
    global D
    global S
    global P
    global NOTVISITED
    global VISITED
    global N

    for step in range(2, N+1):
        # minD回傳一值t使得D[t]為最小
        t = minD()
        S[t] = VISITED

        # 找出經過t點會使路徑縮短的節點
        for I in range(1, N+1):
            if S[I] == NOTVISITED and D[t]+A[t][I] <= D[I]:
                D[I] = D[t] + A[t][I]
                P[I] = t

        output_step()

def minD():
    global Infinite
    global S
    global NOTVISITED
    global N

    t = 0
    minimum = Infinite
    for i in range(1, N+1):
        if S[i] == NOTVISITED and D[i] < minimum:
            minimum = D[i]
            t = i
    return t

# 顯示目前的D陣列與P陣列狀況
def output_step():
    global Infinite
    global N
    global D
    global P

    print('\n\n Step #%d' % step, end = '')
    print('\n============================')
    for i in range(1, N+1):
        print(' D[%d] ' % i, end = '')
    print()

    for i in range(1, N+1):
        if D[i] == Infinite:
            print(' ---- ', end = '')
        else:
            print(' %4d ' % D[i], end = '')
    
    print('\n============================')
    for i in range(1, N+1):
        print(' P[%d] ' % i, end = '')
    print()

    for i in range(1, N+1):
        print(' %4d ' % P[i], end = '')

# 顯示最短路徑
def output_path():
    global Infinite
    global A
    global D
    global P
    global source
    global sink

    node = sink

    # 判斷是否起始頂點等於終點或無路徑至終點
    if sink == source or D[sink] == Infinite:
        print('\nNode %d has no Path to Node %d' % (source, sink), end = '')
        return

    print('\n')
    print(' The shortest Path from V%d to V%d: ' % (source, sink), end = '')
    print('\n------------------------------------------')

    # 由終點開始將上一次經過的中間節點推入堆疊直到起始節點
    print(' V%d' % source, end = '')
    while node != source:
        Push(node)
        node = P[node]
    while node != sink:
        node = Pop()
        print(' --%d--> ' % A[P[node]][node], end = '')
        print('V%d' % node, end = '')
    print('\n Total length: %d' % D[sink])

def Push(value):
    global MAX_V
    global top
    global Stack

    if top >= MAX_V:
        print('Stack overflow!')
        sys.exit(1)
    else:
        top += 1
        Stack[top] = value

def Pop():
    global top
    global Stack

    if top < 0:
        print('Stack empty!')
        sys.exit(1)
    temp = Stack[top]
    top -= 1
    return temp

def main():
    init()
    output_step()
    access()
    output_path()

main()
