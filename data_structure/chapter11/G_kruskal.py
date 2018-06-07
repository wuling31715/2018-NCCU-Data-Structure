# 利用Kruskal's演算法求最小成本擴展樹
# File Name: G_kruskal.py
# Version

import sys

class Edge:
    def __init__(self):
        self.vertex1 = 0
        self.vertex2 = 0
        self.weight = 0
        self.edge_deleted = 0

class Graph:
    def __init__(self):
        self.vertex = [0] * 100
        self.edges = 0

MAX_V = 100 # 最大節點數
TRUE = 1
FALSE = 0

E = [None] * MAX_V
T = Graph()
total_vertex = 0
total_edge = 0
adjmatrix = [[0] * MAX_V for row in range(MAX_V)]

def build_adjmatrix():
    global total_vertex
    global adjmatrix

    try:
        inputStream = open('kruskal.dat', 'r')
    except FileNotFoundError:
        print('File kruskal.dat not found!')
        sys.exit(1)

    # 輸入節點總數
    total_vertex = eval(inputStream.readline().strip('\n'))
    for vi in range(1, total_vertex+1):
        temp = [0] + inputStream.readline().strip('\n').split(' ')
        for vj in range(1, total_vertex+1):
            adjmatrix[vi][vj] = eval(temp[vj])
    inputStream.close()

def adjust():
    global FALSE
    global total_vertex
    global adjmatrix

    for i in range(1, total_vertex+1):
        for j in range(i+1, total_vertex+1):
            weight = adjmatrix[i][j]
            if weight != 0:
                e = Edge()
                e.vertex1 = i
                e.vertex2 = j
                e.weight = weight
                e.edge_deleted = FALSE
                addEdge(e)

def addEdge(e):
    global E
    global total_edge

    total_edge += 1
    E[total_edge] = e

def showEdge():
    global E
    global total_vertex
    global total_edge

    i = 1

    print('Total Vertex = %d' % total_vertex, end = '')
    print('  Total_edge = ', total_edge)
    while i <=  total_edge:
        print('V%d <-----> V%d' % (E[i].vertex1, E[i].vertex2), end = '')
        print('  weight = ', E[i].weight)
        i += 1

def mincostEdge():
    global TRUE
    global FALSE
    global E
    global total_edge

    min = 0
    minweight = 10000000

    for i in range(1, total_edge+1):
        if E[i].edge_deleted == FALSE and E[i].weight < minweight:
            minweight = E[i].weight
            min = i
    E[min].edge_deleted = TRUE
    return E[min]

def kruskal():
    global T
    global total_vertex

    loop = 1

    T.edges = 0

    print('\nMinimum cost spanning tree using Kruskal')
    print('----------------------------------------')

    while T.edges != total_vertex-1:
        e = mincostEdge()
        if cyclicT(e) != 1:
            print('%dth min edge: ' % loop, end = '')
            loop += 1
            print('V%d <-----> V%d' % (e.vertex1, e.vertex2), end = '')
            print('  weight = ', e.weight)

def cyclicT(e):
    global TRUE
    global FALSE
    global T

    v1 = e.vertex1
    v2 = e.vertex2

    T.vertex[v1] += 1
    T.vertex[v2] += 1
    T.edges += 1

    if T.vertex[v1] >= 2 and T.vertex[v2] >= 2:
        T.vertex[v1] -= 1
        T.vertex[v2] -= 1
        T.edges -= 1
        return TRUE
    else:
        return FALSE

def main(): # 主函數
    build_adjmatrix()
    adjust()
    showEdge()
    kruskal()

main()
