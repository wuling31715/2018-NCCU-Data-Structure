# 圖形的追蹤：利用相鄰串列與縱向優先搜尋演算法（DFS）
# File Name: G_dfs.py
# Version

import sys

class Node:
    def __init__(self):
        self.vertex = 0
        self.link = None

MAX_V = 100 # 最大節點數
node = Node()
lastnode = Node()
adjlist = [None] * (MAX_V + 1) # 宣告相鄰陣列
visited = [None] * (MAX_V + 1) # 記錄頂點是否已拜訪
total_vertex = 0

def build_adjlist():
    global node
    global lastnode
    global adjlist
    global visited
    global total_vertex

    weight = 0
    
    try:
        inputStream = open('dfs.dat', 'r')
    except FileNotFoundError:
        print('File dfs.dat not found!')
        sys.exit(1)

    # 讀取節點總數
    total_vertex = eval(inputStream.readline().strip('\n'))
    print('total_vertex = %d' % total_vertex)

    for vi in range(1, total_vertex+1):
        # 設定陣列及各串列起始值
        visited[vi] = False
        adjlist[vi] = Node()
        adjlist[vi].vertex = vi
        adjlist[vi].link = None
  
    # 讀取節點資料
    for vi in range(1, total_vertex+1):
        temp = [0] + inputStream.readline().strip().split(' ') # 讀取一行，以空白分割並放到temp陣列
        for vj in range(1, total_vertex+1):
            # 資料檔以相鄰矩陣格式儲存
            # 以1代表相鄰，0代表不相鄰
            # 將相鄰頂點鏈結在各串列後

            weight = eval(temp[vj])

            if weight != 0:
                node = Node()
                node.vertex = vj
                node.link = None
                lastnode = searchlast(adjlist[vi])
                lastnode.link = node
    inputStream.close()

# 顯示各相鄰串列之資料
def show_adjlist():
    global adjlist

    print('Head adjacency nodes')
    print('--------------------')
    for index in range(1, total_vertex+1):
        print('V%d ' % adjlist[index].vertex, end = '')
        ptr = adjlist[index].link
        while ptr != None:
            print('--> V%d ' % ptr.vertex, end = '')
            ptr = ptr.link
        print()

# 圖形之縱向優先搜尋
def dfs(v):
    global adjlist
    global visited

    print('V%d ' % adjlist[v].vertex, end = '')
    visited[v] = True # 設定v頂點為已拜訪過
    ptr = adjlist[v].link # 拜訪相鄰頂點
    
    while True:
        # 若頂點尚未走訪，則以此頂點為新起始點繼續做縱向優先搜尋法走訪
        # 否則找與其相鄰的頂點，直到所有相連接的節點都已走訪
        w = ptr.vertex
        if visited[w] != True:
            dfs(w)
        else:
            ptr = ptr.link

        if ptr == None:
            break

def searchlast(linklist):
    ptr = linklist
    while ptr.link != None:
        ptr = ptr.link
    return ptr

def main(): # 主函數
    build_adjlist() # 以相鄰串列表示圖形
    show_adjlist() # 顯示串列之資料
    print('\n------Depth First Search------')
    dfs(1) # 圖形之縱向優先搜尋，以頂點1為起始頂點

main()
