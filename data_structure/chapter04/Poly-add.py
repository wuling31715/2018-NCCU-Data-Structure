# 使用降冪排列將兩個格式為ax^b的多項式相加
# File Name: Poly-add.py
# Version

import sys

class Poly:
    def __init__(self):
        self.coef = 0 # 多項式係數
        self.exp = 0  # 多項式指數
        self.next = None

ptr = None
eq_h1 = None
eq_h2 = None
ans_h = None

def input_f():
    global ptr

    eq_h = None
    prev = None
    while True:
        ptr = Poly()
        ptr.next = None

        try:
            ptr.coef = int(input('請輸入係數...'))
        except ValueError:
            print('Not a correct number.')
            print('Try again\n')

        if ptr.coef == 0:
            return eq_h

        try:
            ptr.exp = int(input('請輸入指數...'))
        except ValueError:
            print('Not a correct number.')
            print('Try again\n')

        if eq_h == None:
            eq_h = ptr
        else:
            prev.next = ptr
        prev = ptr

def poly_add():
    global ptr
    global eq_h1
    global eq_h2
    global ans_h

    this1 = eq_h1
    this2 = eq_h2
    prev = None
    while this1 != None or this2 != None: # 當兩多項式皆相加完畢則結束
        ptr = Poly()
        ptr.next = None
        # 第一個多項式指數大於第二個多項式
        if (this1 != None and this2 == None) or this1 != None and this1.exp > this2.exp:
            ptr.coef = this1.coef
            ptr.exp = this1.exp
            this1 = this1.next
        elif this1 == None or this1.exp < this2.exp:
        # 第一個多項式指數小於第二個多項式
            ptr.coef = this2.coef
            ptr.exp = this2.exp
            this2 = this2.next
        else:
            ptr.coef = this1.coef + this2.coef
            ptr.exp = this1.exp
            if this1 != None:
                this1 = this1.next
            if this2 != None:
                this2 = this2.next

        if ptr.coef != 0:
            if ans_h == None:
                ans_h = ptr
            else:
                prev.next = ptr
            prev = ptr
        else:
            ptr = None

def show_poly(head, text):
    node = head
    print('%10s' % text, end = '')
    while node != None:
        print('%dx^%d' % (node.coef, node.exp), end = '')
        if node.next != None and node.next.coef >= 0:
            print('+', end = '')
        node = node.next
    print()

def main():
    global eq_h1
    global eq_h2
    global ans_h

    print('*************************************')
    print(' -- 多項式的格式為：ax^b -- ')
    print('*************************************')
    print('\n<< 第一個多項式（若係數為0，則結束）>>')
    eq_h1 = input_f()
    print('\n<< 第二個多項式（若係數為0，則結束）>>')
    eq_h2 = input_f()
    poly_add()
    print()
    show_poly(eq_h1, '第一個多項式為: ')
    show_poly(eq_h2, '第二個多項式為: ')
    show_poly(ans_h, '相加結果為: ')

main()
