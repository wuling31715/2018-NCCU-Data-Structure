class Combination:

    def method1(a, b):
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
        print('method1: %d' % (c))    

    def method2(a, b):
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
        print('method2: %d' % (c))
