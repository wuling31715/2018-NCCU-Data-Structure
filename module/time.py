import time

class Time:

    def time_measure(function_run, function_name):
        time_start = time.time()
        function_run
        time_end = time.time()
        time_used = time_end - time_start
        function_name = function_name.__name__ 
        return '%s() used time: %f (s)' % (function_name, time_used)

    def test():
        print('Hello World!')

#print(Time.time_measure(Time.test(), Time.test))
