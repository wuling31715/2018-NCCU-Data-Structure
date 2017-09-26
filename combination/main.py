import sys
sys.path.append('..')
from module.time import Time as Time 
from combination import Combination as Combination 

def main(a, b):
    try:
        print(Time.time_measure(Combination.method_1(a, b), Combination.method_1))
    except:
        pass
    try:    
        print(Time.time_measure(Combination.method_2(a, b), Combination.method_2))
    except:
        pass

A = int(input('C\n'))
B = int(input())
main(A, B)
