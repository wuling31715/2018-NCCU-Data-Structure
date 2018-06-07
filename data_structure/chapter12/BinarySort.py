# 二元樹排序
# File Name: BinarySort.py
# Version

class Node_type:
    def __init__(self):
        self.num = 0
        self.lbaby = None
        self.rbaby = None

root = None
tree = None
leaf = None

def binary_sort(data):
    global root
    global tree
    global leaf

    print('\n<< Binary sort >>')
    print('Number : ', end = '')
    for i in range(10):
        print('%4d ' % data[i], end = '')
    print()
    for i in range(60):
        print('-', end = '')

    root = Node_type()
    root.num = data[0] # 建樹根
    root.lbaby = None
    root.rbaby = None

    print('\nSorting: ', end = '')
    output(root)

    leaf = Node_type()
    for i in range(1, 10): # 建樹枝
        leaf.num = data[i]
        leaf.lbaby = None
        leaf.rbaby = None
        find(leaf.num, root)
        if leaf.num > tree.num: # 若比父節點大，則放在右子樹
            tree.rbaby = leaf
        else: # 否則放在左子樹
            tree.lbaby = leaf

        print('\nSorting: ', end = '')
        output(root)

        leaf = Node_type()
    print()

    for i in range(60):
        print('-', end = '')

    print('\nFinal sorted data: ', end = '')
    output(root)

def find(input, papa):
    global tree
    
    if input > papa.num and papa.rbaby != None:
        find(input, papa.rbaby)
    elif input < papa.num and papa.lbaby != None:
        find(input, papa.lbaby)
    else:
        tree = papa

# 印出資料
def output(node): # 用中序追蹤將資料印出
    if node != None:
        output(node.lbaby)
        print('%4d ' % node.num, end = '')
        output(node.rbaby)

def main():
    data = [18, 2, 20, 34, 12, 32, 6, 16, 25, 10]
    binary_sort(data)

main()
