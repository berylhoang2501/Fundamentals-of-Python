import calendar
from datetime import datetime

while True:
    str_date = input('Nhập ngày mua hàng theo định dạng dd/mm/yy: ')
    list_date = str_date.split('/')
    _year = int(list_date[2])
    _month = int(list_date[1])
    _day = int(list_date[0])
    _index = calendar.weekday(_year, _month, _day)
    tuple_day = "Thứ 2", "Thứ 3", "Thứ 4", "Thứ 5", "Thứ 6", "Thứ 7", "Chủ nhật"

    ten_hang = input('Nhập tên hàng: ')
    so_luong = int(input('Nhập số lượng: '))
    don_gia = float(input('Nhập đơn giá: '))

    thanh_tien = don_gia * so_luong

    print('HOÁ ĐƠN MUA HÀNG')
    print('Thành tiền: {:,} x {} = {:,} VNĐ'.format(don_gia, so_luong, thanh_tien))

    ngay_mua = datetime.strptime(str_date, "%d/%m/%Y")

    giam_gia = 0
    if ngay_mua.weekday() == 4 and ngay_mua.day == 13:  
        giam_gia = thanh_tien * 0.15  

    print('Giảm giá: {:,} VNĐ'.format(giam_gia))  
    print('Thanh toán: {:,} - {:,} = {:,} VNĐ '.format(thanh_tien,giam_gia,thanh_tien - giam_gia)) 
    print('Ngày xuất hoá đơn:', tuple_day[_index], 'ngày', str_date) 




 