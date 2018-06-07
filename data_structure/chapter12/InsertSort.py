# 插入排序
# File Name: InsertSort.py
# Version

def Insertion_Sort(data):
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
    print('First data is %d\n' % data[0])

    # 當資料小於第一筆，則插於前方，否則與後面資料比對找出插入位置
    for base in range(1, size):
        temp = data[base]
        compare = base
        print('Inserting data is ', data[base])
        while compare>0 and data[compare-1] > temp:
            data[compare] = data[compare-1]
            data[compare-1] = temp
            compare -= 1

        print('After #%d insertion: ' % base, end = '')
        for i in range(base+1):
            print(data[i], ' ', end = '')
        print('\n')

def main():
    data = []
    Insertion_Sort(data)

main()
