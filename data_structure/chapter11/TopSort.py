# 拓撲排序
# File Name: TopSort.py
# Version

import sys

# 定義資料結構
class Node:
    def __init__(self):
        self.vertex = 0
        self.link = None

MAX_V = 100
N = 0
place = 0
visited = [None] * (MAX_V+1) # 記錄頂點是否已拜訪

# 宣告相鄰串列
Top_order = [0] * (MAX_V+1)
adjlist = [None] * (MAX_V+1)

def build_adjlist():
    global N
    global adjlist

    weight = 0
    t1 = -1
    t2 = -1
    done = False

    try:
        inputStream = open('top_sort.dat', 'r')
    except Exception:
        print('File top_sort.dat not found!')
        sys.exit(1)

    # 讀取節點總數
    N = eval(inputStream.readline().strip('\n'))

    # 設定陣列及各串列起始值
    for vi in range(1, N+1):
        adjlist[vi] = Node()
        adjlist[vi].vertex = vi
        adjlist[vi].link = None

    # 讀取節點資料
    while done == False:
        try:
            temp = inputStream.readline().strip('\n').split(' ')
            vi = eval(temp[0])
            vj = eval(temp[1])
        except Exception:
            done = True

        # 避免讀入重覆資料
        if vi != t1 or vj != t2:
            node = Node()
            node.vertex = vj
            node.link = None
            if adjlist[vi].link == None:
                adjlist[vi].link = node
            else:
                lastnode = searchlast(adjlist[vi])
                lastnode.link = node
            t1 = vi
            t2 = vj

    inputStream.close()

def show_adjlist():
    global adjlist
    global N

    print('\nHead adjacency nodes')
    print('--------------------')
    for v in range(1, N+1):
        print('V%d ' % adjlist[v].vertex, end = '')
        ptr = adjlist[v].link
        while ptr != None:
            print('--> V%d ' % ptr.vertex, end = '')
            ptr = ptr.link
        print()

def topological():
    global N
    global visited
    global place

    for v in range(1, N+1):
        visited[v] = False
    place = N
    for v in range(1, N+1):
        if visited[v] != True:
            top_sort(v)

def top_sort(k):
    global visited
    global adjlist
    global place
    global Top_order

    w = 0
    visited[k] = True

    # 拜訪v相鄰頂點
    ptr = adjlist[k].link
    while ptr != None:
        w = ptr.vertex
        if visited[w] != True:
            top_sort(w)
        ptr = ptr.link
    
    place -= 1
    Top_order[place] = k

def searchlast(linklist):
    ptr = linklist
    while ptr.link != None:
        ptr = ptr.link
    return ptr

def show_topological():
    global N
    global Top_order

    print('\n------Topological order sort------')
    for i in range(N):
        print('V%d ' % Top_order[i], end = '')
    print()

def main():
    build_adjlist()
    show_adjlist()
    topological()
    show_topological()

main()
