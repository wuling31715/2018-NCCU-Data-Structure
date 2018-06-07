# 利用m-way search tree處理資料的新增、刪除與輸出
# File Name: MwayTree.py
# Version

import sys

class TreeNode: # 定義資料欄位
    def __init__(self):
        self.iD = 0 # 輸出時識別節點
        self.n = 0 # 節點內的鍵值數
        self.key = [0] * 3 # 節點鍵值
        self.link = [None] * 3 # 節點子鏈結

MAX = 3 # 設定此為3-WAY TREE的最大節點數
ptr = None
root = None
node = None
prev = None
parent = None
replace = None
id_seq = ''

# 新增函數——新增一筆資料
def insert_f():
    add_num = int(input('\n   Please enter insert number: '))
    create(add_num)
    print()

# 刪除函數——刪除一筆資料
def delete_f():
    global root
    global node

    del_num = 0
    ans = 0

    if root == None: # 當樹根為空，顯示錯誤訊息
        print('\n   No data found!!\n')
    else:
        del_num = int(input('\n   Please enter delete number: '))
        ans = search_num(del_num) # 搜尋資料是否存在
        if ans == 0: # 當資料不存在，顯示錯誤訊息
            print('   Number %d not found!!\n' % del_num)
        else:
            removes(node, ans)
            print('   Number %d deleted!!\n' % del_num)

# 輸出函數——將M-WAY TREE內的所有資料輸出
def display_f():
    global root
    global id_seq

    if root == None: # 當樹根為空，顯示錯誤訊息
        print('\n   No data found!!\n')
    else:
        id_seq = 'a' # 節點編號由a開始
        preorder_id(root) # 給予每個節點編號
        print('\n The data of M-way search tree is listing below: ')
        print('=============================================')
        preorder_num(root) # 輸出節點資料
        print('=============================================')

# 將資料加入，並調整為M-WAY TREE，NUM為新增之資料鍵值
def create(num):
    global root
    global ptr
    global node
    global prev
    
    ans = 0
    i = 0
    
    if root == None: # 樹根為空的狀況
        initial()
        ptr.key[1] = num
        ptr.n += 1
        root = ptr
    else:
        ans = search_num(num) # 搜尋資料是否已存在
        if ans != 0: # 資料存在，則顯示錯誤訊息
            print('   Number %d has existed!!\n' % num)
        else:
            node = search_node(num) # 找尋插入點
            if node != None: # 插入點還有空間存放資料的狀況
                i = 1
                while i < MAX-1:
                    if num < node.key[i]:
                        break
                    i += 1
                moveright(i, num)
            else: # 新增一個節點加入資料的狀況
                initial()
                ptr.key[1] = num
                ptr.n += 1
                i = 1
                while i < MAX:
                    if num < prev.key[i]:
                        break
                    i += 1
                prev.link[i-1] = ptr
    print('%10d has been inserted!' % num)

# 將資料移除，並調整為M-WAY TREE，node_TEMP為刪除資料所在節點
# LOCATION為資料在節點中的位置
def removes(node_temp, location):
    global root
    global node
    global prev
    global parent
    global replace

    node = node_temp
    replace = find_next(node.link[location]) # 找尋替代之後繼節點
    if replace == None: # 沒有後繼節點的狀況
        replace = find_prev(node.link[location-1])    # 找尋替代之前行節點
        if replace == None: # 沒有前行節點的狀況
            moveleft(location)
            replace = node
            if node.n == 0: # 刪除資料後，節點內資料為0的處理
                if node == root: # 當節點為根的狀況
                    root = None
                else: # 節點不是根，則調整鏈結
                    for i in range(parent.n+1):
                        if node == parent.link[i]:
                            parent.link[i] = None
                            break
        else: # 有前行節點的狀況
            # 以前行節點的資料代替刪除資料
            node.key[location] = replace.key[replace.n]
            parent = prev
            removes(replace, replace.n) # 移除替代資料
    else: # 有後繼節點的狀況
        # 以後繼節點的資料代替刪除資料
        node.key[location] = replace.key[1]
        parent = prev
        removes(replace, 1) # 移除替代資料

# 初始化節點——新增一個節點，將其所有鏈結指向NONE，設其節點數為0
def initial():
    global MAX
    global ptr

    ptr = TreeNode()
    for i in range(MAX):
        ptr.link[i] = None
    ptr.n = 0

# 搜尋節點位置——搜尋NUM，存在則回傳NUM在節點中的位置，不存在則回傳0
def search_num(num):
    global root
    global node
    global prev
    global parent

    n_temp = 0

    node = root
    while node != None:
        parent = prev
        prev = node
        i = 1
        done = 0
        while i <= node.n:
            if num == node.key[i]:
                return i # 找到NUM，回傳其在節點中的位置
            if num < node.key[i]:
                node = node.link[i-1]
                done = 1
                break
            i += 1
        if done == 0:
            node = node.link[i-1]
    return 0 # 沒有找到則回傳0

# 搜尋節點——尋找插入NUM的節點，並回傳插入節點
def search_node(num):
    global MAX
    global root
    
    node_temp = root

    while node_temp != None:
        if node_temp.n < MAX-1:
            return node_temp # 找到有多餘空間存放NUM，則回傳此節點
        else:
            i = 1
            done = 0
            while i < MAX:
                if node_temp.n < i:
                    break
                if num < node_temp.key[i]:
                    node_temp = node_temp.link[i-1]
                    done = 1
                    break
                i += 1
            if done == 0:
                node_temp = node_temp.link[i-1]
    return node_temp # 若沒有找到有多餘空間存放NUM的節點，回傳NONE

# 將節點內資料右移——將節點資料右移至INDEX位置，並將NUM插入
def moveright(index, num):
    global node
    
    i = node.n + 1

    while i > index: # 資料右移至INDEX處
        node.key[i] = node.key[i-1]
        node.link[i] = node.link[i-1]
        i -= 1
    node.key[i] = num # 插入NUM
    # 調整NUM左右鏈結
    if node.link[i-1] != None and node.link[i-1].key[0] > num:
        node.link[i] = node.link[i-1]
        node.link[i-1] = None
    node.n += 1

# 將節點內資料左移——將節點資料從INDEX位置左移
def moveleft(index):
    global node

    for i in range(index, node.n): # 節點資料左移
        node.key[i] = node.key[i+1]
        node.link[i] = node.link[i+1]
    node.n -= 1

# 尋找後繼節點——尋找node_TEMP的後繼節點，回傳找到的後繼節點
def find_next(node_temp):
    global node
    global prev

    prev = node
    if node_temp != None:
        while node_temp.link[0] != None:
            prev = node_temp
            node_temp = node_temp.link[0]
    return node_temp

# 尋找前行節點——尋找node_TEMP的前行節點，回傳找到的前行節點
def find_prev(node_temp):
    global MAX
    global node
    global prev

    prev = node
    if node_temp != None:
        while node_temp.link[MAX-1] != None:
            prev = node_temp
            node_temp = node_temp.link[MAX-1]
    return node_temp

# 給予節點編號——使用前序遞迴方式給予每個節點編號
def preorder_id(tree):
    global id_seq
    
    if tree != None:
        tree.iD = id_seq
        id_seq = chr(ord(id_seq) + 1)
        for i in range(tree.n+1):
            preorder_id(tree.link[i])

# 輸出資料——使用前序遞迴方式輸出節點資料
def preorder_num(tree):

    i = 0
    link_id = ''

    if tree != None:
        # 當節點鏈結為NONE，則現實鏈結為0
        if tree.link[0] == None:
            link_id = '0'
        else:
            link_id = tree.link[0].iD
        print(' %s, %d, %s' % (tree.iD, tree.n, link_id), end = '')
        for i in range(1, tree.n+1):
            if tree.link[i] == None:
                link_id = '0'
            else:
                link_id = tree.link[i].iD
            print(', (%d, %s)' % (tree.key[i], link_id), end = '')
            i += 1
        print()
        for i in range(tree.n+1):
            preorder_num(tree.link[i])

# 主函數
def main():
    option = 0

    while True:
        print('******** m-way search tree ********')
        print('*          <1> Login              *')
        print('*          <2> Logout             *')
        print('*          <3> Show               *')
        print('*          <4> Exit               *')
        print('***********************************')

        try:
            option = eval(input('        Choice: '))
        except ValueError:
            print('Not a correct number.')
            print('Try again\n')

        if option == 1:
            insert_f() # 新增函數
        elif option == 2:
            delete_f() # 刪除函數
        elif option == 3:
            display_f() # 輸出函數
        elif option == 4:
            sys.exit(0)

main()
