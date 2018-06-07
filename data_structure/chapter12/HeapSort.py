# 堆積排序
# File Name: HeapSort.py
# Version

def heap_sort(data):
    print('\n<< Heap sort >>')
    print('Number : ', end = '')
    for k in range(1, 11):
        print('%2d ' % data[k], end = '')
    print()

    for k in range(60):
        print('-', end = '')

    i = 10
    while i > 0:
        adjust(data, i, 10)
        i -= 1

    print('\nHeap   : ', end = '')
    for k in range(1, 11):
        print('%2d ' % data[k], end = '')

    i = 9
    while i > 0:
        data[1], data[i+1] = data[i+1], data[1] # 將樹根和最後的節點交換
        adjust(data, 1, i) # 再重新調整為堆積樹
        print('\nSorting: ', end = '')
        for k in range(1, 11):
            print('%2d ' % data[k], end = '')
        i -= 1
    print()

    for k in range(60):
        print('-', end = '')

    print('\nFinal sorted data: ', end = '')
    for k in range(1, 11):
        print(data[k], ' ', end = '')

def adjust(data, i, n): # 將資料調整為堆積樹
    done = 0
    k = data[i]
    j = 2 * i
    while j <= n and done == 0:
        if j < n and data[j] < data[j+1]:
            j += 1
        if k >= data[j]:
            done = 1
        else:
            data[j//2] = data[j]
            j *= 2
    data[j//2] = k

def main():
    data = [0, 27, 7, 80, 5, 67, 18, 62, 24, 58, 25]
    heap_sort(data)

main()
