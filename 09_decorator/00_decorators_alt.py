"""
حل تمرین‌های دوره «آموزش پایتون جامع» تدریس شده توسط جادی در وب‌سایت مکتبخونه.
لینک دوره: https://maktabkhooneh.org/course/%D8%A2%D9%85%D9%88%D8%B2%D8%B4-%D8%A8%D8%B1%D9%86%D8%A7%D9%85%D9%87-%D9%86%D9%88%DB%8C%D8%B3%DB%8C-%D8%A8%D8%A7-%D9%BE%D8%A7%DB%8C%D8%AA%D9%88%D9%86-%D9%85%D9%82%D8%AF%D9%85%D8%A7%D8%AA%DB%8C-mk346/

این راه‌حل‌ها در بهار ۱۴۰۴ ارائه شده و موفق به کسب نمره کامل (۱۰۰) شده‌اند.

لطفاً از این کدها تنها در راستای یادگیری استفاده نمایید.
در صورت اعلام هرگونه نارضایتی از سوی جادی یا مکتبخونه، این مخزن به حالت خصوصی (Private) درخواهد آمد و از دسترس خارج می‌شود.

ارادتمند،  
سعید زینل‌پور
"""


def my_timer(f):
    def wrapper (*args, **kwargs):
        import datetime
        start_time = datetime.datetime.now()
        result = f(*args, **kwargs)
        end_time = datetime.datetime.now()

        exec_time = end_time - start_time
        exec_time = exec_time.total_seconds()
        
        return exec_time , result
    return wrapper

@my_timer
def count_fun(n = 100000):
    my_list = list(range(1, n+1))
    return my_list

@my_timer
def print_res(result):
    return print(result)

n = int(input(""))

exec_time, result = count_fun(n)

print_exec = print_res(result)

print(print_exec, exec_time)