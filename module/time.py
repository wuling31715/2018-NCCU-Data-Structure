from datetime import datetime

class Time:

    def time_measure(function):
        time_start = datetime.now()
        function()
        time_end = datetime.now()
        time_used = str(time_end - time_start)
        function_name = function.__name__ 
        return '%s() used time: %s (s)' % (function_name, time_used)

    def test():
        time.sleep(3)
        print('Hello World!')

#print(Time.time_measure(Time.test))
