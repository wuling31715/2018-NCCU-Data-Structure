# 基數排序
# File Name: RadixSort.py
# Version

def radix_sort(data, order):
    n = 1
    k = 0
    temp = [[None] * 10 for i in range(10)]

    while n <= 100:
        for i in range(10):
            lsd = (data[i]//n) % 10
            temp[lsd][order[lsd]] = data[i] # 依餘數將資料分類
            order[lsd] += 1

        print('\nSorting: ', end = '')
        for i in range(10):
            if order[i] != 0:
                for j in range(order[i]):
                    # 依分類後的順序將資料重新排列
                    data[k] = temp[i][j]
                    print('%5d ' % data[k], end = '')
                    k += 1
            order[i] = 0
        n *= 10
        k = 0

def main():
    data = [199, 228, 326, 118, 879, 882, 76, 32, 291, 56]
    order = [0] * 10

    print('\n<< Radix sort >>')
    print('\nNumber : ', end = '')
    for i in range(10):
        print('%5d ' % data[i], end = '')
    print()

    for i in range(70):
        print('-', end = '')

    radix_sort(data, order)
    print()

    for i in range(70):
        print('-', end = '')

    print('\nFinal sorted data: ', end = '')
    for i in range(10):
        print('%5d ' % data[i], end = '')

main()