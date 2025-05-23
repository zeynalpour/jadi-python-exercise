"""
حل تمرین‌های دوره «آموزش پایتون جامع» تدریس شده توسط جادی در وب‌سایت مکتبخونه.
لینک دوره: https://maktabkhooneh.org/course/%D8%A2%D9%85%D9%88%D8%B2%D8%B4-%D8%A8%D8%B1%D9%86%D8%A7%D9%85%D9%87-%D9%86%D9%88%DB%8C%D8%B3%DB%8C-%D8%A8%D8%A7-%D9%BE%D8%A7%DB%8C%D8%AA%D9%88%D9%86-%D9%85%D9%82%D8%AF%D9%85%D8%A7%D8%AA%DB%8C-mk346/

این راه‌حل‌ها در بهار ۱۴۰۴ ارائه شده و موفق به کسب نمره کامل (۱۰۰) شده‌اند.

لطفاً از این کدها تنها در راستای یادگیری استفاده نمایید.
در صورت اعلام هرگونه نارضایتی از سوی جادی یا مکتبخونه، این مخزن به حالت خصوصی (Private) درخواهد آمد و از دسترس خارج می‌شود.

ارادتمند،  
سعید زینل‌پور
"""

def pick_evens(*args):
    next_arr = []
    for x in args:
        if x % 2 == 0:
            next_arr.append(x)
    return next_arr


def split_to_int(inp):
    rs = inp.split(" ") if inp else []
    next_rs = []
    for x in range(len(rs)):
        if rs[x]:
            next_rs.append(int(rs[x])) 
    return next_rs

input_string = input("")
input_int_arr = split_to_int(input_string)
output = pick_evens(*input_int_arr)

print(output)