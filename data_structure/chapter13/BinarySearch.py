# 二元搜尋''
# File Name: BinarySearch.py
# Version

input_ = 0

def binary_search(data):
    global input_

    m = 0
    n = 10
    ok = 0
    cnt = 0
    l = 1

    m = (1 + n) // 2 # 鍵值在第M筆
    while l <= n and ok == 0:
        print('\nData when searching: ', end = '')
        cnt += 1
        print('# %d is %d!' % (cnt, data[m]), end = '')
        if data[m] > input_: # 欲搜尋的資料小於鍵值，則資料在鍵值的前面
            n = m - 1
            print(' ---> %d is bigger than %d' % (input_, data[m]), end = '')
        elif data[m] < input_: # 否則資料在鍵值的後面
            l = m + 1
            print(' ---> %d is bigger than %d' % (input_, data[m]), end = '')
        else:
            print('\n\nFound %d is the %dth record in data!' % (input_, m))
            ok = 1
        m = (l + n) // 2
    if ok == 0:
        print('\n\nSorry, %d not found!' % input_)

def main():
    global input_

    data = [0, 21, 23, 29, 38, 44, 57, 64, 75, 82, 98]

    print('\n<< Binary search >>')
    print('Sorted data: ', end = '')
    for i in range(1, 11):
        print(data[i], ' ', end = '')
    print()

    while True:
        input_ = int(input('\nWhat number do you want to search? '))
        
        print('\nSearching......')
        binary_search(data)

        more = input('要繼續搜尋嗎？（y/n）： ')
        ch = more
        if ch == 'n':
            break
main()
