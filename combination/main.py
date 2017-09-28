import sys
sys.path.append('..')
from module.time import Time as time 
from combination import Combination as combination 

def main(a, b):
    print(time.time_measure(combination.method2(a, b), combination.method2))

A = int(input('C\n'))
B = int(input())
main(A, B)

