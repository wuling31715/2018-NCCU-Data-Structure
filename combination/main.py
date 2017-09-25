import time

def method_1(a, b):
    x = 1
    y = 1
    z = 1
    for i in range(1, a + 1):
        x = x * i
    for i in range(1, b + 1):
        y = y * i 
    for i in range(1, a - b + 1):
        z = z * i
    c = int(x / (y * z))    
    print('Method1: %d' % (c))    

def method_2(a, b):
    x = 1
    y = 1
    d = a - b
    if d > b:
        for i in range(d + 1, a + 1):
            x = x * i
        for i in range(1, b + 1):
            y = y * i
    else:
        for i in range(b + 1, a + 1):
            x = x * i
        for i in range(1, d + 1):
            y = y * i
    c = int(x / y)
    print('Method2: %d' % (c))

def main(a, b):
    time_start = time.time()
    method_1(a, b)
    time_end = time.time()
    time_used_1 = time_end - time_start
    time_start = time.time()
    method_2(a, b)
    time_end = time.time()
    time_used_2 = time_end - time_start
    print('Method1 Time Used: %f (S)' % (time_used_1))
    print('Method2 Time Used: %f (S)' % (time_used_2))

A = int(input('C\n'))
B = int(input())

main(A, B)
