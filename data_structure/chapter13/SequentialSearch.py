# 循序搜尋
# File Name: SequentialSearch.py
# Version

input_ = 0

def sequential_search(data):
    global input_

    i = 0
    while i < 10: # 依序搜尋資料
        print('Data ', end = '')
        print('#%-2d is %2d' % (i+1, data[i]))
        if input_ == data[i]:
            break
        i += 1
    if i == 10:
        print('\n\nSorry, ', input_, ' not found!')
    else:
        print('\n\nFound, ', input_, ' is the ', (i+1), ' record in data!')

def main():
    global input_

    data = [35, 75, 23, 44, 57, 12, 29, 64, 38, 82]
    print('\n<< Sequential search >>')
    print('\nData: ', end = '')
    for i in range(10):
        print(data[i], ' ', end = '')
    print()

    while True:
        input_ = int(input('\nWhat number do you want to search? '))
        
        print('\nSearching......')
        sequential_search(data)

        more = input('要繼續搜尋嗎？（y/n）： ')
        ch = more
        if ch == 'n':
            break

main()
