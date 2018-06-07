# 使用環狀佇列處理資料──新增、刪除、輸出
# File Name： CirQue.py
# Version

import sys

MAX = 10
cq = [''] * MAX
front = MAX - 1
rear = MAX - 1
tag = 0 # 當tag為0時，表示沒有存放資料，若為1，則表示有存放資料

# 新增函數
def enqueue_f():
    global MAX
    global cq
    global front
    global rear
    global tag

    if front == rear and tag == 1: # 當佇列已滿，則顯示錯誤
        print('\n   此佇列已滿！')
    else:
        rear = (rear + 1) % MAX
        cq[rear] = input('\n 請輸入一筆資料（字串格式）：')

        if front == rear:
            tag = 1
    print()

# 刪除函數
def dequeue_f():
    global MAX
    global cq
    global front
    global rear
    global tag

    if front == rear and tag == 0: # 當佇列沒有資料存在，則顯示錯誤
        print('\n   此佇列是空的！\n')
    else:
        front = (front + 1) % MAX
        print('\n   %s 已被刪除！' % cq[front])

        if front == rear:
            tag = 0
        print()

# 輸出函數
def list_f():
    global MAX
    global cq
    global front
    global rear
    global tag

    count = 0

    if front == rear and tag == 0:
        print('\n   此佇列是空的！\n')
    else:
        print('\n\n   佇列有下列資料')
        print('********************')
        i = (front + 1) % MAX
        while i != rear:
            print('   ', end = '')
            print(cq[i])
            count += 1
            i = (i + 1) % MAX
        print('   ', end = '')
        print(cq[i])
        print('********************')

        count += 1
        print('   共有%d筆資料。\n\n' % count)

# 主函數
def main():
    option = 0

    while True:
        print('***** 環狀佇列的選單 *****')
        print('      1. Insert         ')
        print('      2. Delete         ')
        print('      3. List           ')
        print('      4. Exit           ')
        print('************************')

        try:
            option = eval(input('   請選擇您要執行的項目：'))
        except ValueError:
            print('Not a correct number.')
            print('Try again\n')

        if option == 1:
            enqueue_f() # 新增函數
        elif option == 2:
            dequeue_f() # 刪除函數
        elif option == 3:
            list_f() # 輸出函數
        else:
            sys.exit(0)

main()
