from libs.functions import *
duong_dan='files/quanlykho.csv'
while True:
    print('CHƯƠNG TRÌNH QUẢN LÝ KHO')
    print('1. In dữ liệu lưu trên file')
    print('5. Thống kê mặt hàng có số lượng nhiều nhất kho')
    
    tac_vu=input('Chọn 1 tác vụ tương ứng: ')
    if tac_vu=='1':
        noi_dung_file=read_file(duong_dan)
        print_file(noi_dung_file)
    elif tac_vu=='5':
        noi_dung_file=read_file(duong_dan)
        dong_tieu_de=noi_dung_file.pop(0)
        ket_qua=tim_max(noi_dung_file)
        print_file(ket_qua)
    else:
        break
