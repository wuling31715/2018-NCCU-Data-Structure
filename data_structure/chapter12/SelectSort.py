# 選擇排序
# File Name: SelectSort.py
# Version

def select_sort(data):
    size = 0
    i = 0
    
    print('\nPlease enter number to sort (enter 0 when end): ') # 要求輸入資料直到輸入為零
    while True:
        i += 1
        data.append(int(input('#%d number: ' % i)))
        if data[size] == 0:
            break
        size += 1

    for i in range(60):
        print('-', end = '')
    print()

    print('\nOriginal data: ', end = '')
    for i in range(size):
        print(data[i], ' ', end = '')
    print('\n')

    sorting(data, size)

    for i in range(60):
        print('-', end = '')

    print('\nFinal sorted data : ', end = '')
    for i in range(size):
        print('%d ' % data[i], end = '')

def sorting(data, size):
    for base in range(size-1): # 將目前資料與後面資料中最小的對調
        min = base
        for compare in range(base+1, size):
            if data[compare] < data[min]:
                min = compare
        print('#%d selected data is: %d' % (base+1, data[min]))

        # 處理交換的動作
        data[min], data[base] = data[base], data[min]

        print('Partial sorted data: ', end = '')
        for i in range(size):
            print(data[i], ' ', end = '')
        print('\n')

def main():
    data = []
    select_sort(data)

main()
