# 合併排序
# File Name: MergeSort.py
# Version

data1 = []
data2 = []
data3 = []

def merge_sort():
    global data1
    global data2
    global data3

    size1 = 0
    size2 = 0
    i = 0
    
    print('\nPlease enter data 1 to sort (enter 0 when end): ') # 要求輸入資料直到輸入為零
    while True:
        i += 1
        data1.append(int(input('#%d number: ' % i)))
        if data1[size1] == 0:
            break
        size1 += 1

    print('\nPlease enter data 2 to sort (enter 0 when end): ') # 要求輸入資料直到輸入為零
    while True:
        i += 1
        data2.append(int(input('#%d number: ' % i)))
        if data2[size2] == 0:
            break
        size2 += 1

    # 先使用選擇排序將兩數列排序，再作合併
    select_sort(data1, size1)
    select_sort(data2, size2)

    for i in range(60):
        print('-', end = '')
    print()

    print('\nData 1: ', end = '')
    for i in range(size1):
        print(data1[i], ' ', end = '')

    print('\nData 2: ', end = '')
    for i in range(size2):
        print(data2[i], ' ', end = '')
    print()

    for i in range(60):
        print('-', end = '')
    print()

    sorting(size1, size2)

    for i in range(60):
        print('-', end = '')

    print('\nFinal sorted data : ', end = '')
    for i in range(size1+size2):
        print('%d ' % data3[i], end = '')

def select_sort(data, size):
    for base in range(size-1):
        min = base
        for compare in range(base+1, size):
            if data[compare] < data[min]:
                min = compare
        data[min], data[base] = data[base], data[min]

def sorting(size1, size2):
    global data1
    global data2
    global data3

    data1[size1] = 32767
    data2[size2] = 32767
    arg1 = 0
    arg2 = 0
    for arg3 in range(size1+size2):
        if data1[arg1] < data2[arg2]: # 比較兩數列，資料小的先存於合併後的數列
            data3.append(data1[arg1])
            arg1 += 1
            print('This step takes %d from data1' % data3[arg3])
        else:
            data3.append(data2[arg2])
            arg2 += 1
            print('This step takes %d from data2' % data3[arg3])
        print('Sorting...: ', end = '')
        for i in range(arg3+1):
            print(data3[i], ' ', end = '')
        print('\n')

def main():
    merge_sort()

main()
