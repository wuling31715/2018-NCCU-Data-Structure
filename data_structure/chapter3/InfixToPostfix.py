# 將數學式子由中序表示法轉為後序表示法
# File Name: InfixToPostfix.py
# Version

MAX = 20
infix_q = [''] * 20

def infix_to_postfix():
    global MAX
    global infix_q

    rear = top = i = 0
    index = -1
    stack_t = [''] * MAX # 用以儲存還不必輸出的運算子

    str_ = str(input('請輸入一中序運算式：'))

    while i < len(str_):
        index += 1
        infix_q[index] = str_[i]
        i += 1

    infix_q[index+1] = '#' # 於佇列結束時加入#為結束符號

    print('Postfix expression: ', end = '')

    stack_t[top] = '#' # 於堆疊最底下加入#為結束符號

    for ctr in range(index+2):
        if infix_q[ctr] == ')': # 輸入為)，則輸出堆疊內運算子，直到堆疊內為(
            while stack_t[top] != '(':
                print(stack_t[top], end = '')
                top -= 1
            top -= 1
        
        elif infix_q[ctr] == '#': # 輸入為#，則將堆疊內還未輸出的運算子輸出
            while stack_t[top] != '#':
                print(stack_t[top], end = '')
                top -= 1
        
        # 輸入為運算子，若小於TOP在堆疊中所指運算子，則將堆疊所指運算子輸出
        # 若大於等於TOP在堆疊中所指運算子，則將輸入之運算子放入堆疊
        elif infix_q[ctr] == '(' \
          or infix_q[ctr] == '^' \
          or infix_q[ctr] == '*' \
          or infix_q[ctr] == '/' \
          or infix_q[ctr] == '+' \
          or infix_q[ctr] == '-':
            while compare(stack_t[top], infix_q[ctr]) == 1:
                print(stack_t[top], end = '')
                top -= 1
            top += 1
            stack_t[top] = infix_q[ctr]

        # 輸入為運算元，則直接輸出
        else:
            print(infix_q[ctr], end = '')

# 比較兩運算子優先權，若輸入運算子小於堆疊中運算子，則回傳值為1，否則為0
def compare(stack_o, infix_o):
    # 在中序表示法佇列及暫存堆疊中，運算子的優先順序表，其優先權值為INDEX//2
    infix_priority = []
    stack_priority = []
    index_s = 0
    index_i = 0

    infix_priority.append('#')
    infix_priority.append(')')
    infix_priority.append('+')
    infix_priority.append('-')
    infix_priority.append('*')
    infix_priority.append('/')
    infix_priority.append('^')
    infix_priority.append(' ')
    infix_priority.append('(')

    stack_priority.append('#')
    stack_priority.append('(')
    stack_priority.append('+')
    stack_priority.append('-')
    stack_priority.append('*')
    stack_priority.append('/')
    stack_priority.append('^')
    stack_priority.append(' ')

    while stack_priority[index_s] != stack_o:
        index_s += 1

    while infix_priority[index_i] != infix_o:
        index_i += 1

    if (index_s // 2) >= (index_i // 2):
        return 1
    else:
        return 0

def main(): # 主函數
    print('\n***************************')
    print('       -- 有效運算子 --       ')
    print(' ^：次方')
    print(' *：成       	/：除')
    print(' +：加       	-：減')
    print(' (：左括號    	)：右括號')
    print('*****************************')
    
    infix_to_postfix()

main()
