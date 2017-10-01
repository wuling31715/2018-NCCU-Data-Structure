#import sys
#sys.path.append('..')
import time 
from module.timer import Timer as timer 

def method1():
    time.sleep(1)

def method2():
    time.sleep(2)

print(timer.count(method1))
print(timer.count(method2))
        
