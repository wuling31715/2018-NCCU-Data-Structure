# 利用遞迴方式計算N階乘
# File Name: Factor.py
# Version

def Factorial(n):
    if n == 1:
        return 1
    else:
        return n * Factorial(n - 1)

def main(): # 主函數
    ch = ''
    n = 0

    print('-----Factorial counting Using Recursive-----')
    while True:
        try:
            n = int(input('\nEnter a number to count n!: '))
        except ValueError:
            print('Not a correct number.')
            print('Try again\n')

        print('%d! = %d\n' % (n, Factorial(n)))

        ch = input('Continue (y/n) ? ')
        if ch != 'y':
            break

main()