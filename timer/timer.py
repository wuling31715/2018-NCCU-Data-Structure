from datetime import datetime

class Timer:
    def now():
        return datetime.now()

    def count_function(function):
        time_start = datetime.now()
        function()
        time_end = datetime.now()
        time_used = str(time_end - time_start)
        function_name = function.__name__ 
        return '%s(): %s' % (function_name, time_used)


