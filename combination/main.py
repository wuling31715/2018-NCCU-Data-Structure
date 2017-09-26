import sys
sys.path.append('..')
from module.time import Time as Time 
from combination import Combination as Combination 

def main(a, b):
    try:
        print(Time.time_measure(Combination.method2(a, b), Combination.method2))
    except:
        print('error')
    try:    
        print(Time.time_measure(Combination.method1(a, b), Combination.method1))
    except:
        print('error')

A = int(input('C\n'))
B = int(input())
main(A, B)
