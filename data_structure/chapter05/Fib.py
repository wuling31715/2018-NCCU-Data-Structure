# 利用遞迴方式計算費氏數列
# File Name: Fib.py
# Version

def Fibonacci(n):
    if n == 0 or n == 1: # 第0項與第1項為1
        return 1
    else:
        return Fibonacci(n - 1) + Fibonacci(n - 2)

def main(): # 主函數
    ch = ''
    n = 0

    print('-----Fibonacci numbers Using Recursive-----')

    while True:
        try:
            n = int(input('\nEnter a number(n>=0) : '))
        except ValueError:
            print('Not a correct number.')
            print('Try again\n')

        # n值大於0
        if n < 0:
            print('Number must be > 0\n')
        else:
            print('Fibonacci(%d) = %d\n' % (n, Fibonacci(n)))
    
        ch = input('Continue (y/n) ? ')
    
        if ch != 'y':
            break

main()
