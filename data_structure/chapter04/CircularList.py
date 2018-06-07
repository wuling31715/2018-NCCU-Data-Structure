# 環狀串列的加入、刪除、修改及輸出
# File Name: CircularList.py
# Version

import sys

class Student:
    def __init__(self):
        self.name = ''
        self.score = 0
        self.next = None

ptr = None        
current = None
prev = None

head = Student()        
head.next = head
    
def insert_f():
    global head
    global ptr
    global current
    global prev


    ptr = Student()
    print('\n\n************ Insert Node ************')
    ptr.name = input('  Please enter student name : ')
    ptr.score = eval(input('  Please enter student score : '))
    print('\n***************************************\n')
    prev = head
    current = head.next
    while current != head and current.score >= ptr.score:
        prev = current
        current = current.next
    ptr.next = current
    prev.next = ptr
        
def delete_f():
    global head
    global current
    global prev

    del_name = ''
        
    if head.next == head:
        print('\n     No student record !!')
    else:
        print('\n\n************ Delete Node ************\n')
        del_name = input(' Please enter student name : ')
            
        prev = head
        current = head.next
        while current != head and del_name != current.name:
            prev = current
            current = current.next
        if current != head:
            prev.next = current.next
            current = None
            print(' Student %s record deleted' % del_name)
        else:
            print(' Student %s not found' % del_name)
    print('\n***************************************\n')

def modify_f():
    global head
    global current
    global prev

    if head.next == head:
        print('\n     No student record !!\n')
    else:
        print('\n\n************ Modify Node ************')
        modify_name = input(' Please enter student name: ')

        prev = head
        current = head.next
        while current != head and modify_name != current.name:
            prev = current
            current = current.next
        
        if current != head: # 找到要修改的資料，顯示該筆資料的原始資料
            print('\n   Student name: %s' % current.name)
            print('   Student score: %d\n' % current.score)
            prev.next = current.next # 把舊的資料刪除
            current = None
            # 重新加入新的資料
            newscore = eval(input(' Please enter new score: '))
            ptr = Student()
            ptr.next = None
            ptr.name = modify_name
            ptr.score = newscore
            prev = head
            current = head.next
            while current != head and current.score >= ptr.score:
                prev = current
                current = current.next
            ptr.next = current
            prev.next = ptr
        else:
            print('\n Student %s not found!\n' % modify_name) # 找不到資料

        
def display_f():
    global head
    global current

    count = 0
        
    if head.next == head:
        print('\n     No student record !!')
    else:
        print('\n\n************ Display Node ************')
        print('%-15s %5s' % ("NAME", "SCORE"))
        print('------------------------------------------')
        current = head.next
        while (current != head):
            print('%-15s %-3d' % (current.name, current.score))
            count += 1
            current = current.next
        print('------------------------------------------')
        print(' Total %d record(s) found !!' % count)
    print('\n****************************************\n')
        
def main():
    option = 0
    
    while True:
        print('***** Circular list operation *****')
        print('          <1> Insert               ')
        print('          <2> Delete               ')
        print('          <3> Modify               ')
        print('          <4> List                 ')
        print('          <5> Exit                 ')
        print('***********************************')
        
        try:
            option = int(input('          Choice : '))
        except ValueError:
            print()
            print('Not a correct number.')
            print('Try again\n')
            
        if option == 1:
            insert_f()
        elif option == 2:
            delete_f()
        elif option == 3:
            modify_f()
        elif option == 4:
            display_f()
        elif option == 5:
            sys.exit(0)

main()
