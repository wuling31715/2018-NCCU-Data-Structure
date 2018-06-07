# 利用AVL-TREE處理學生資料的新增、刪除、修改與輸出
# File Name: AVLtree.py
# Version

import sys

# 定義一個Node的資料結構(Class)，其資料含兩個子鏈結，儲存姓名、分數、節點BF值
class Student:
    def __init__(self):
        self.name = '' # 姓名
        self.score = 0 # 分數
        self.bf = 0 # 節點BF值
        self.llink = None # 節點左子鏈結
        self.rlink = None # 節點右子鏈結

root = None
ptr = None
current = None
prev = None
pivot = None
pivot_prev = None
nodecount = 0 # 用來計算node個數

# 新增函數
def insert_f():
    global nodecount

    name_t = ''
    score_t = 0

    print('\n********** Insert Node **********')
    name_t = input('   Please enter student name: ')
    score_t = eval(input('   Please enter student score: '))

    print('\n          New node          ')
    print('------------------------------')
    print('   Name : %s     Score: %d' % (name_t, score_t))
    print('******************************')

    nodecount += 1 # 將node加1

    sort_f(name_t, score_t)

# 處理AVL-TREE之資料輸入
def sort_f(name_t, score_t):
    global ptr
    global root
    global current
    global prev
    global pivot

    op = 0
    current = root

    while current != None and name_t != current.name:
        if name_t < current.name: # 插入資料小於目前位置，則往左移
            prev = current
            current = current.llink
        else: # 若大於目前位置，則往右移
            prev = current
            current = current.rlink

    # 找到插入位置，無重複資料存在
    if current == None or name_t != current.name:
        ptr = Student() # 配置記憶體
        ptr.name = name_t
        ptr.score = score_t
        ptr.llink = None
        ptr.rlink = None
        if root == None: # ROOT不存在，則將ROOT指向插入資料
            root = ptr
        elif ptr.name < prev.name:
            prev.llink = ptr
        else:
            prev.rlink = ptr
        bf_count(root)
        pivot = pivot_find()
        if pivot != None: # PIVOT存在，則須改善為AVL-TREE
            op = type_find()
            if op == 11:
                type_ll()
            elif op == 22:
                type_rr()
            elif op == 12:
                type_lr()
            elif op == 21:
                type_rl()
        bf_count(root) # 重新計算每個節點的BF值
    else: # 欲插入資料KEY已存在，則顯示錯誤
        print('   ADD New Node error !!')
        print('   Student <%s> has existed !' % name_t)

# 計算BF值，使用後序法逐一計算
def bf_count(trees):
    if trees != None:
        bf_count(trees.llink)
        bf_count(trees.rlink)
        # BF值計算方式為左子樹高減去右子樹高
        trees.bf = height_count(trees.llink) - height_count(trees.rlink)

def height_count(trees):
    if trees == None:
        return 0
    elif trees.llink == None and trees.rlink == None:
        return 1
    elif height_count(trees.llink) > height_count(trees.rlink):
        return 1 + height_count(trees.llink)
    else:
        return 1 + height_count(trees.rlink)

def pivot_find():
    global root
    global current
    global prev
    global pivot
    global pivot_prev
    global nodecount
    
    current = root
    pivot = None

    for i in range(nodecount):
        # 當BF值的絕對值小於等於1，則將PIVOT指向此節點
        if current.bf < -1 or current.bf > 1:
            pivot = current
            if pivot != root:
                pivot_prev = prev
            print('Current pivot name: ', current.name)
        if current.bf > 0: # 左子樹的高度較高
            prev = current
            current = current.llink
        elif current.bf < 0: # 右子樹的高度較高
            prev = current
            current = current.rlink

    return pivot

def type_find():
    global current
    global pivot
    
    op_r = 0
    current = pivot
    for i in range(2):
        if current.bf > 0: # 左子樹的高度較高
            current = current.llink
            if op_r == 0:
                op_r += 10
            else:
                op_r += 1
        elif current.bf < 0: # 右子樹的高度較高
            current = current.rlink
            if op_r == 0:
                op_r += 20
            else:
                op_r += 2

    # 回傳值11、22、12、21分別代表LL、RR、LR、RL型態
    return op_r

# LL型
def type_ll():
    global root
    global pivot
    global pivot_prev

    pivot_next = pivot.llink
    temp = pivot_next.rlink
    
    pivot_next.rlink = pivot
    pivot.llink = temp
    
    if pivot == root:
        root = pivot_next
    elif pivot_prev.llink == pivot:
        pivot_prev.llink = pivot_next
    else:
        pivot_prev.rlink = pivot_next

# RR型
def type_rr():
    global root
    global pivot
    global pivot_prev

    pivot_next = pivot.rlink
    temp = pivot_next.llink

    pivot_next.llink = pivot
    pivot.rlink = temp

    if pivot == root:
        root = pivot_next
    elif pivot_prev.llink == pivot:
        pivot_prev.llink = pivot_next
    else:
        pivot_prev.rlink = pivot_next

# LR型
def type_lr():
    global root
    global pivot
    global pivot_prev

    pivot_next = pivot.llink
    temp = pivot_next.rlink

    pivot.llink = temp.rlink
    pivot_next.rlink = temp.llink
    
    temp.llink = pivot_next
    temp.rlink = pivot

    if pivot == root:
        root = temp
    elif pivot_prev.llink == pivot:
        pivot_prev.llink = temp
    else:
        pivot_prev.rlink = temp

# RL型
def type_rl():
    global root
    global pivot
    global pivot_prev

    pivot_next = pivot.rlink
    temp = pivot_next.llink

    pivot.rlink = temp.llink
    pivot_next.llink = temp.rlink
    
    temp.rlink = pivot_next
    temp.llink = pivot

    if pivot == root:
        root = temp
    elif pivot_prev.llink == pivot:
        pivot_prev.llink = temp
    else:
        pivot_prev.rlink = temp

# 輸出函數
def list_f():
    global root

    if root == None: # 無資料存在，則顯示錯誤
        print('\n   No student record exist !!')
    else:
        list_data() # 中序列印

# 將Node資料以中序方式印出
def list_data():
    global root

    print('\n******** List Data ********')
    print('%-15s %-10s' % ("Name", "Score"))
    print('-----------------------------')
    inorder(root)
    print('-----------------------------')

# 中序使用遞迴
def inorder(trees):
    try:
        inorder(trees.llink)
        print('%-16s' % trees.name, end = '')
        print('%3d' % trees.score)
        inorder(trees.rlink)
    except BaseException:
        None

# 修改函數
def modify_f():
    global root
    global current

    name_t = ''
    score_t = 0

    if root == None: # 無資料存在，則顯示錯誤
        print('\n   No student record exist !!')
    else:
        print('\n******** Modify Node ********')
        name_t = input('   Please enter student name: ')

        current = root
        while current != None and name_t != current.name:
            if name_t < current.name:
                current = current.llink
            else:
                current = current.rlink

        #若找到欲更改資料，則列出原資料，並要求輸入新的資料
        if current != None:
            print('\n   Student name: ', current.name)
            print('   Student score: ', current.score)
            print('\n*****************************')
            current.score = eval(input('   Please enter new score: '))
            print('   Data updated successfully')
        else: # 找不到資料，則顯示錯誤
            print('\n   Student : ', name_t, ' Not Found !!!')

    print()

# 刪除函數
def delete_f():
    global root
    global current
    global prev
    global pivot
    global nodecount

    clear = None
    op = 0
    name_t = ''
    tempn = ''

    if root == None: # 無資料存在，則顯示錯誤
        print('\n   No student record exist !!')
    else:
        print('\n******** Delete Node ********')
        name_t = input('   Please enter student name: ')
        tempn = name_t
        current = root
        # 尋找刪除點
        while current != None and name_t != current.name:
            # 若刪除資料鍵值小於目前所在資料，則往左子樹
            if name_t < current.name:
                prev = current
                current = current.llink
            # 否則往右子樹
            else:
                prev = current
                current = current.rlink

        # 找到欲刪除資料的狀況
        if current != None and name_t == current.name:
            # 當欲刪除資料底下無左右子樹存在的狀況
            if current.llink == None and current.rlink == None:
                clear = current
                if name_t == root.name: # 欲刪除資料為ROOT
                    root = None
                else:  # 若不為ROOT，則判斷其為左子樹或右子樹
                    if name_t < prev.name:
                        prev.llink = None
                    else:
                        prev.rlink = None
                clear = None
            else:
                if current.llink != None:  # 以左子樹最大點代替刪除資料
                    clear = current.llink
                    while clear.rlink != None:
                        prev = clear
                        clear = clear.rlink
                    current.name = clear.name
                    current.score = clear.score
                    if current.llink == clear:
                        current.llink = clear.llink
                    else:
                        prev.rlink = clear.llink
                else:  # 以右子樹最小點代替刪除資料
                    clear = current.rlink
                    while clear.llink != None:
                        prev = clear
                        clear = clear.llink
                    current.name = clear.name
                    current.score = clear.score
                    if current.rlink == clear:
                        current.rlink = clear.rlink
                    else:
                        prev.llink = clear.rlink
                clear = None

            bf_count(root)
            if root != None: # 若ROOT不存在，則無需作平衡改善
                pivot = pivot_find() # 尋找PIVOT所在節點
                while pivot != None:
                    op = type_find()
                    if op == 11:
                        type_ll()
                    elif op == 22:
                        type_rr()
                    elif op == 12:
                        type_lr()
                    elif op == 21:
                        type_rl()
                    bf_count(root)
                    pivot = pivot_find()

            nodecount -= 1 # 將node減1
            print('\n   Student %s has been deleted' % tempn)
        else: # 找不到資料，則顯示錯誤
            print('\n   Student %s not found !!!' % tempn)

# 主函數
def main():
    option = 0

    while True:
        print()
        print('******** AVLtree Program ********')
        print('*        <1> Insert Node        *')
        print('*        <2> Delete Node        *')
        print('*        <3> Modify Node        *')
        print('*        <4> List Node          *')
        print('*        <5> Exit               *')
        print('*********************************')

        try:
            option = eval(input('\n         Choice: '))
        except ValueError:
            print('Not a correct number.')
            print('Try again\n')

        if option == 1:
            insert_f() # 新增函數
        elif option == 2:
            delete_f() # 刪除函數
        elif option == 3:
            modify_f() # 修改函數
        elif option == 4:
            list_f()   # 輸出函數
        elif option == 5:
            sys.exit(0)

main()
