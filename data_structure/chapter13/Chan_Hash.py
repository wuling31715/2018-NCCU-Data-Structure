# 雜湊法：使用連結串列處理碰撞
# File Name: Chan_Hash.py
# Version

import sys

class Student:
    def __init__(self):
        self.id = 0
        self.name = ''
        self.link = None

MAX_NUM = 100 # 最大資料筆數
PRIME = 97 # 最大MAX_NUM之質數
NOTEXISTED = None
Hashtab = [None] * MAX_NUM # 建立雜湊表串列

# 雜湊函數：以除法運算求出記錄應儲存的位址
def hashfun(key):
    global PRIME

    return key % PRIME

def insert():
    global NOTEXISTED
    global Hashtab

    newnode = Student()
    index = 0

    # 輸入記錄
    newnode.link = None
    newnode.id = int(input('\nEnter ID: '))
    newnode.name = input('Enter name: ')

    # 利用雜湊函數求得記錄位址
    index = hashfun(newnode.id)
    # 判斷該串列是否為空，若為空則建立此鏈結串列
    if Hashtab[index] == None:
        Hashtab[index] = newnode
        print('加入成功！')
    elif search(Hashtab[index], newnode) == NOTEXISTED: # 搜尋節點是否已存在串列中，如未存在則將此節點加入串列前端
        newnode.link = Hashtab[index]
        Hashtab[index] = newnode
        print('加入成功！')
    else:
        print('此筆已存在...')
    print()

# 刪除節點函數
def delete():
    global NOTEXISTED
    global Hashtab

    node = Student()
    index = 0

    node.id = int(input('\nEnter ID: '))

    # 利用雜湊函數轉換記錄位址
    index = hashfun(node.id)
    # 判斷該串列是否為空，若為空則建立此鏈結串列
    if Hashtab[index] == None:
        print('Record not existed ...\n')
        return
    node = search(Hashtab[index], node)
    if node == NOTEXISTED:
        print('Record not existed ...\n')
    else:
        # 搜尋節點是否已存在串列中
        # 如未存在則將此節點加入串列前端
        print('ID: %d, Name: %s' % (node.id, node.name))

        # 詢問使用者是否真的要刪除此資料
        ch = input('確定要刪除嗎？（y/n）： ')

        if ch == 'y':
            if node == Hashtab[index]:
                Hashtab[index] = None
            else:
                node_parent = Hashtab[index]
                while node_parent.link.id != node.id:
                    node_parent = node_parent.link
                node_parent.link = node.link
            print('It has been deleted\n')

# 搜尋節點函數
# 如找到節點則回傳指向該節點之指標
# 否則回傳None
def search(linklist, Node):
    global NOTEXISTED

    ptr = linklist
    while ptr.id != Node.id and ptr.link != None:
        ptr = ptr.link
    
    if ptr == None:
        return NOTEXISTED
    else:
        return ptr

# 查詢節點函數
def query():
    global NOTEXISTED
    global Hashtab

    query_node = Student()
    
    query_node.id = int(input('\nEnter ID: '))

    index = hashfun(query_node.id)
    # 搜尋節點
    if Hashtab[index] == None:
        print('Record not existed...\n')
        return

    query_node = search(Hashtab[index], query_node)

    if query_node == NOTEXISTED:
        print('Record not existed...\n')
    else:
        print('ID: %d, Name: %s' % (query_node.id, query_node.name))
    print()

# 顯示節點函數
# 從雜湊串列尋找是否有節點存在
def show():
    global Hashtab

    flag = 0
    ptr = Student()

    print('\n%-15s %-15s' % ('ID', 'NAME'))
    print('-------------------------')
    for i in range(MAX_NUM):
        # 串列不為空，則將整個串列顯示出來
        if Hashtab[i] != None:
            flag = 1
            ptr = Hashtab[i]
            while ptr != None:
                print('%-15d %-15s' % (ptr.id, ptr.name))
                ptr = ptr.link

    if flag == 0:
        print('No record in hashing table')
    print()

def main():
    while True:
        print()
        print('****** Hashing table ******')
        print('       <1> Insert          ')
        print('       <2> Delete          ')
        print('       <3> Show            ')
        print('       <4> Search          ')
        print('       <5> Exit            ')
        print('***************************')
        option = input('\n     Choice: ')

        if option == '1':
            insert() # 新增函數
        elif option == '2':
            delete() # 刪除函數
        elif option == '3':
            show() # 輸出函數
        elif option == '4':
            query() # 查詢函數
        elif option == '5':
            sys.exit(0)

main()
