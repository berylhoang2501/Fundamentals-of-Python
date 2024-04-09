from libs.functions import *
duong_dan='files/hoadon.csv'
while True:
    print('CHƯƠNG TRÌNH QUẢN LÝ BÁN HÀNG')
    print('1. Xem tất cả đơn hàng đang lưu')
    print('2. Thêm đơn hàng mới')
    print('3. Thống kê các đơn hàng theo mã')
    tac_vu=input('Chọn 1 tác vụ tương ứng: ')
    if tac_vu=='1':
        noi_dung_file=read_file(duong_dan)
        print_file(noi_dung_file)
    elif tac_vu=='2':
        danh_sach_don_hang = read_file(duong_dan)
        them_don_hang_moi(danh_sach_don_hang, duong_dan)
        print('Lưu thành công!')
    elif tac_vu == '3':
        noi_dung_file = read_file(duong_dan)
        thong_ke(noi_dung_file)
    else:
        break