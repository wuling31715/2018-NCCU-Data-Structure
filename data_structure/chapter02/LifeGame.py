# 生命細胞遊戲實作
# File Name: LifeGame.py
# Version

MAXROW = 10
MAXCOL = 25
DEAD = 0
ALIVE = 1
map_ = [[DEAD for col in range(MAXCOL)] for row in range(MAXROW)]
newmap = [[ALIVE for col in range(MAXCOL)] for row in range(MAXROW)]
Generation = 0

def init():
    global MAXROW
    global MAXCOL
    global DEAD
    global ALIVE
    global map_
    global newmap

    row = 0
    col = 0

    print('Game of life Program ')
    print('Enter (x, y) where (x, y) is a living cell')
    print('0 <= x <= %d, 0 <= y <= %d' % (MAXROW-1, MAXCOL-1))
    print('Terminate with (x, y) = (-1, -1)')

    # 輸入活細胞之位置，以(-1, -1)結束輸入
    while row != -1 or col != -1:
        row = int(input('x-->'))
        col = int(input('y-->'))
        if ( 0 <= row and row < MAXROW and 0 <= col and col < MAXCOL):
            map_[row][col] = ALIVE
        elif row == -1 and col == -1:
            print('Input is terminated')
        else:
            print('(x, y) exceeds map range!')

def Neighbors(row, col):
    global MAXROW
    global MAXCOL
    global map_
    global newmap
    
    count = 0
    
    # 計算每一個cell的鄰居個數
    # 因為cell本身亦被當做鄰居計算
    # 故最後還要調整

    for r in range(row-1, row+2):
        for c in range(col-1, col+2):
            if r < 0 or r >= MAXROW or c < 0 or c >= MAXCOL:
                continue
            if map_[r][c] == ALIVE:
                count += 1

    # 調整鄰居個數
    if map_[row][col] == ALIVE:
        count -= 1
    return count

# 顯示目前細胞狀態
def output_map():
    global MAXROW
    global MAXCOL
    global map_
    global newmap
    global Generation

    space = ' '
    print(space, '\nGame of life cell status')
    Generation += 1
    print('------Generation %d------' % Generation)
    for row in range(MAXROW):
        print()
        print(space)
        for col in range(MAXCOL):
            if map_[row][col] == ALIVE:
                print('@', end = '')
            else:
                print('-', end = '')

def access():
    global MAXROW
    global MAXCOL
    global DEAD
    global ALIVE
    global map_
    global newmap

    ans = 'y'

    while ans == 'y':
        # 計算每一個(row, col)之cell的鄰居個數
        # 依此個數決定其下一代是生是死。
        # 將下一代的map_暫存在newmap以防overwrite map_。
        for row in range(MAXROW):
            for col in range(MAXCOL):
                if Neighbors(row, col) == 0 \
                or Neighbors(row, col) == 1 \
                or Neighbors(row, col) == 4 \
                or Neighbors(row, col) == 5 \
                or Neighbors(row, col) == 6 \
                or Neighbors(row, col) == 7 \
                or Neighbors(row, col) == 8:
                    newmap[row][col] = DEAD
                elif Neighbors(row, col) == 2:
                    newmap[row][col] = map_[row][col]
                elif Neighbors(row, col) == 3:
                    newmap[row][col] = ALIVE

        Copymap() # 將newmap copy to map_
                
        while True:
            ans = input('\n\nContinue next Generation ? (y/n): ')
            if ans == 'y' or ans == 'n':
                break

        if ans == 'y':
            output_map()
            
# 將newmap copy至map_中
def Copymap():
    global MAXROW
    global MAXCOL
    global map_
    global newmap

    for row in range(MAXROW):
        for col in range(MAXCOL):
            map_[row][col] = newmap[row][col]

def main(): # 主函數
    init() # 起始map
    output_map()
    access()

main()
