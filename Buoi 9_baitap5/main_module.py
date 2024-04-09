from libs.functions import *
duong_dan='files/donhang.csv'
while True:
    print('CHƯƠNG TRÌNH QUẢN LÝ ĐƠN HÀNG')
    print('1. In dữ liệu lưu trên file')
    print('2. Thêm đơn hàng mới')
     
    tac_vu=input('Chọn 1 tác vụ tương ứng: ')
    if tac_vu=='1':
        noi_dung_file=read_file(duong_dan)
        print_file(noi_dung_file)
    elif tac_vu=='2':
        noi_dung_file=read_file(duong_dan)
        don_hang_moi=them_don_hang(noi_dung_file)
        #print(đơn hàng mới)
        write_file(duong_dan,don_hang_moi)
        print('Đặt hàng thành công!')
    else:
        break