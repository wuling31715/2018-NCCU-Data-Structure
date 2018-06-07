# 泡沫排序
# File Name: BubbleSort.py
# Version

def bubble_sort(data):    
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

    sorting(data, size)

    for i in range(60):
        print('-', end = '')

    print('\nSorted data : ', end = '')
    for i in range(size):
        print('%d ' % data[i], end = '')

def sorting(data, size):
    for base in range(size-1): # 讓資料兩兩比較，將小的置於前
        flag = 0
        # 印出第幾次的Pass
        print('#%d pass: ' % (base+1))
        for compare in range(size-base-1):
            if data[compare] > data[compare+1]:
                flag = 1
                data[compare], data[compare+1] = data[compare+1], data[compare]

            # 印出每一次的Compare
            print('#%d compare: ' % (compare+1), end = '')
            for k in range(size-base):
                print('%d ' % data[k], end = '')
            print()

        # 印出每一次Pass最後的資料
        print('#%d pass sorted data: ' % (base+1), end = '')
        for k in range(size):
            print('%d ' % data[k], end ='')
        print('\n')
        if flag != 1:
            break

def main():
    data = []
    bubble_sort(data)

main()
