# Viết chương trình nhập vào ngày theo định dạng dd/mm/yyyy 
# In ra màn hình ngày của bạn nhập vào là ngày thứ mấy?

import calendar
str_date=input('Nhập ngày cần kiểm tra theo định dạng dd/mm/yy: ')
list_date=str_date.split('/')
_year=int(list_date[2])
_month=int(list_date[1])
_day=int(list_date[0])
_index=calendar.weekday(_year,_month,_day)
tuple_day="Thứ 2","Thứ 3","Thứ 4","Thứ 5","Thứ 6","Thứ 7","Chủ nhật"
print(str_date,'là ngày',tuple_day[_index])

