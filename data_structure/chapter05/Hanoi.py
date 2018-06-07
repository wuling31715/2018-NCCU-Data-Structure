# 利用遞迴方式求河內塔問題之解
# File Name: Hanoi.py
# Version

# Rules :
#     河內塔問題目的乃在三根柱子中，將n個盤子從
#     A柱子搬到C柱中，每次只移動一盤子，而且必須
#     遵守每個盤子都比其上面的盤子還要大的原則。

# Ans :
#     河內塔問題的想法必須針對最底端的盤子。
#     我們必須先把A柱子頂端n-1個盤子想辦法（借助C柱）移至B柱子
#     然後才能將最底端的盤子移至C柱。
#     此時C有最大的盤子，B總共n-1個盤子，A柱則無。
#     只要再借助A柱子，將B柱n-1個盤子移往C柱即可：

#     HanoiTower(n-1, A, C, B)
#     將A頂端n-1個盤子借助C移至B
#     HanoiTower(n-1, B, A, C)
#     將B上的n-1個盤子借助A移至C

def HanoiTower(n, _from, _aux, _to):
    if n == 1:
        print('Move disk %d from %c --> %c' % (n, _from, _to))
    else:
        # 將A上n-1個盤子借助C移至B
        HanoiTower(n-1, _from, _to, _aux)
        print('Move disk %d from %c --> %c' % (n, _from, _to))

        # 將B上n-1個盤子借助A移至C
        HanoiTower(n-1, _aux, _from, _to)

def main(): # 主函數
    ch = ''
    n = 0
    A = 'A'
    B = 'B'
    C = 'C'

    print('-----Hanoi Tower Implementation-----')
    #輸入共有幾個盤子在A柱子中
    while True:
        try:
            n = int(input('How many disks in A ? '))
        except ValueError:
            print('Not a correct number.')
            print('Try again\n')

        if n == 0:
            print('No disk to move')
        else:
            HanoiTower(n, A, B, C)

        ch = input('\nContinue (y/n) ? ')

        if ch != 'y':
            break

main()