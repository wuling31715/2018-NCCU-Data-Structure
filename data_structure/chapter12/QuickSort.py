# 快速排序
# File Name: QuickSort.py
# Version

def quick_sort(data):
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

    sorting(data, 0, size-1, size)

    for i in range(60):
        print('-', end = '')

    print('\nFinal sorted data: ', end = '')
    for i in range(size):
        print(data[i], ' ', end = '')

def sorting(data, left, right, size):
    #left與right分別代表欲排序資料兩端
    if left < right:
        lbase = left + 1
        while data[lbase] < data[left]:
            if lbase+1 > size:
                break
            lbase += 1
        rbase = right
        while data[rbase] > data[left]:
            rbase -= 1
        while lbase < rbase: # 若lbase小於rbase，則兩資料對調
            data[lbase], data[rbase] = data[rbase], data[lbase]
            lbase += 1
            while data[lbase] < data[left]:
                lbase += 1
            rbase -= 1
            while data[rbase] > data[left]:
                rbase -= 1
        data[left], data[rbase] = data[rbase], data[left] # 此時lbase大於rbase，則rbase的資料與第一筆對調
        
        print('Sorting: ', end = '')
        for i in range(size):
            print('%4d' % data[i], end = '')
        print()

        sorting(data, left, rbase-1, size)
        sorting(data, rbase+1, right, size)

def main():
    data = []
    quick_sort(data)

main()