# 謝耳排序
# File Name: ShellSort.py
# Version

MAX = 9

def shell_sort(data):
    global MAX

    incr = MAX // 2
    while incr > 0:
        for i in range(incr+1, MAX+1):
            j = i - incr
            while j > 0:
                if data[j] > data[j+incr]: # 比較每部分的資料
                    # 大小順序不對則交換
                    data[j], data[j+incr] = data[j+incr], data[j]
                    j = j - incr
                else:
                    j = 0
        print('\nSorting: ', end = '')
        for i in range(1, MAX+1):
            print('%3d ' % data[i], end = '')
        incr = incr // 2

def main():
    data = [0, 39, 11, 48, 5, 77, 18, 70, 25, 55]

    print('\n<< Shell sort >>')
    print('Number : ', end = '')
    for i in range(1, 10):
        print('%3d ' % data[i], end = '')
    print()
    
    for k in range(60):
        print('-', end = '')

    shell_sort(data)
    print()

    for k in range(60):
        print('-', end = '')

    print('\nFinal sorted data: ', end = '')
    for i in range(1, MAX+1):
        print('%3d ' % data[i], end = '')

main()