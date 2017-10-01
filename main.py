#import sys
#sys.path.append('..')
import time 
from module.time import Time as timer 

def method1():
    time.sleep(1)

def method2():
    time.sleep(2)

print(timer.time_measure(method1))
print(timer.time_measure(method2))
        
