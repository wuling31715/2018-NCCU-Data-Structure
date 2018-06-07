# 利用Heap處理會員推出資料──新增、刪除、輸出
# File Name: HeapTree.py
# Version

import sys

MAX = 100
heap_tree = [0] * MAX # Heap陣列
last_index = 0 # 最後一筆資料的index

# 新增函數
def insert_f():
    global MAX
    global last_index

    if last_index >= MAX-1: # 資料數超過上限，顯示錯誤訊息
        print('\n   Login members are more than %d !!' % MAX - 1)
        print('   Please wait for a Minute ...')
        
    id_temp = int(input('\n   Please enter login ID number: '))
    create(id_temp) # 建立Heap
    print('     Login successfully!!')

# 刪除函數
def delete_f():
    global last_index

    id_temp = 0
    del_index = 0

    if last_index < 1: # 無資料存在，顯示錯誤訊息
        print('\n   No member to logout!!')
        print('   Please check again!!')
    else:
        id_temp = int(input('\n   Please enter logout ID number: '))
        del_index = search(id_temp)
        if del_index == 0: # 沒找到資料，顯示錯誤訊息
            print('   ID number not found!!')
        else:
            removes(del_index) # 刪除資料，並調整Heap
            print('   ID number ', id_temp, ' logout!!')

# 輸出函數
def display_f():
    global last_index
    option = ''

    if last_index < 1: # 無資料存在，顯示錯誤訊息
        print('\n   No member to show!!\n')
    else:
        print()
        print('********************')
        print('   <1> increase') # 選擇第一項為由小到大排列
        print('   <2> decrease') # 選擇第二項為由大到小排列
        print('********************')
        while True:
            try:
                option = input('\n   Please enter your option: ')
            except ValueError:
                print()
                print('Not a correctly number.')
                print('Try again\n')
            if (option == '1' or option == '2'):
                break
        show(option)

# 建立資料於Heap，ID_TEMP為新增資料
def create(id_temp):
    global last_index
    global heap_tree
    last_index += 1
    heap_tree[last_index] = id_temp # 將資料新增於最後
    adjust_u(heap_tree, last_index) # 調整新增資料

# 從Heap中刪除資料，INDEX_TEMP為欲刪除資料之INDEX
def removes(index_temp):
    global last_index
    global heap_tree

    # 以最後一筆資料代替刪除資料
    heap_tree[index_temp] = heap_tree[last_index]
    heap_tree[last_index] = 0
    last_index -= 1
    if last_index > 1: # 當資料筆數大於1筆，則做調整
        # 當替代資料大於其PARENT NODE，則往上調整
        if heap_tree[index_temp] > heap_tree[index_temp//2] and index_temp > 1:
            adjust_u(heap_tree, index_temp)
        else: # 替代資料小於其CHILDREN NODE，則往下調整
            adjust_d(heap_tree, index_temp, last_index-1)

# 印出資料於螢幕
def show(op):
    global last_index
    global heap_tree
    heap_temp = []
    tChar = ''

    # 將Heap資料複製到另一個陣列作排序工作
    heap_temp = [i for i in heap_tree]
    # 將陣列調整為由小到大排列
    c_index = last_index - 1
    while c_index > 0:
        exchange(heap_temp, 1, c_index+1)
        adjust_d(heap_temp, 1, c_index)
        c_index -= 1
    print('\n\n   ID number')
    print(' **********************')
    # 選擇第一種方式輸出，以遞迴方式輸出──使用堆疊
    # 選擇第二種方式輸出，以遞迴方式輸出──使用佇列
    if op == '1':
        for c_index in range(1, last_index + 1):
            print(' ', heap_temp[c_index])
    elif op == '2':
        c_index = last_index
        while c_index > 0:
            print(' ', heap_temp[c_index])
            c_index -= 1

    print(' **********************')
    print(' Total member: ', last_index, '\n')

# 從下而上調整資料，index為目前資料在陣列之INDEX
def adjust_u(temp, index):
    while (index > 1): # 將資料往上調整至根為止
        if temp[index] <= temp[index//2]: # 資料調整完畢就跳出，否則交換資料
            break
        else:
            exchange(temp, index, index//2)
        index //= 2

# 從上而下調整資料，index1為目前資料在陣列之INDEX，index2為最後一筆資料在陣列之INDEX
def adjust_d(temp, index1, index2):
    # id_temp記錄目前資料，index_temp則是目前資料之CHILDREN NODE的INDEX
    id_temp = temp[index1]
    index_temp = index1 * 2
    # 當比較資料之INDEX不大於最後一筆資料之INDEX，則繼續比較
    while index_temp <= index2:
        if index_temp < index2 and temp[index_temp] < temp[index_temp+1]:
            index_temp += 1 # index_temp記錄目前資料之CHILDREN NODE中較大者
        if id_temp >= temp[index_temp]: # 比較完畢則跳出，否則交換資料
            break
        else:
            temp[index_temp//2] = temp[index_temp]
            index_temp *= 2
    temp[index_temp//2] = id_temp

# 交換傳來之id1及id2儲存之資料
def exchange(arr, id1, id2):
    id_temp = arr[id1]
    arr[id1] = arr[id2]
    arr[id2] = id_temp

# 尋找陣列中id_temp所在
def search(id_temp):
    global heap_tree
    
    for c_index in range(1, len(heap_tree)):
        if id_temp == heap_tree[c_index]:
            return c_index # 找到則回傳資料在陣列中之INDEX
    return 0 # 沒找到則回傳0

def main():
    option = ''
    while True:
        print('\n****** HeapTree Program ******')
        print('       <1> Login              ')
        print('       <2> Logout             ')
        print('       <3> Show               ')
        print('       <4> Exit               ')
        print('******************************')
        
        try:
            option = input('      Choice : ')
        except ValueError:
            print('Not a correct number.')
            print('Try again\n')

        if option == '1':
            insert_f() # 新增函數
        elif option == '2':
            delete_f() # 刪除函數
        elif option == '3':
            display_f() # 輸出函數
        elif option == '4':
            sys.exit(0)
        else:
            print('     Invalid option!!')

main()
