# 使用堆疊處理資料──新增、刪除、輸出
# File Name： Stack.py
# Version

import sys

MAX = 10
st = [''] * MAX
top = -1

def push_f(): # 新增函數
    global MAX
    global st
    global top

    if top >= MAX - 1: # 當堆疊已滿，則顯示錯誤
        print('\n   堆疊是滿的！')
    else:
        top += 1
        st[top] = input('\n 請輸入一筆資料（字串的格式）：')
    print()

def pop_f(): # 刪除函數
    global st
    global top

    if top < 0: # 當堆疊沒有資料存在，則顯示錯誤
        print('\n   堆疊是空的！')
    else:
        print('\n   %s 已被刪除！' % st[top])
        top -= 1
    print()

def list_f(): # 輸出函數
    global st
    global top

    count = 0
    
    if top < 0:
        print('\n   堆疊是空的！')
    else:
        print('\n\n 堆疊有下列的資料：')
        print('-------------------')
        i = top
        while i >= 0:
            print(' ', end = '')
            print(st[i])
            count += 1
            i -= 1
        print('-------------------')
        print(' 堆疊共有%d筆資料。\n' % count)
    print()

def main(): # 主函數
    option = 0

    while True:
        print('***** 堆疊的選單 *****')
        print('      1. Insert      ')
        print('      2. Delete      ')
        print('      3. List        ')
        print('      4. Exit        ')
        print('*********************')

        try:
            option = eval(input('   請選擇您要執行的項目：'))
        except ValueError:
            print('Not a correct number.')
            print('Try again\n')

        if option == 1:
            push_f() # 新增函數
        elif option == 2:
            pop_f() # 刪除函數
        elif option == 3:
            list_f() # 輸出函數
        else:
            sys.exit(0)

main()
