from libs.functions import *

duong_dan = 'files/diem.csv'

while True:
    print('CHƯƠNG TRÌNH QUẢN LÝ TÀI KHOẢN')
    print('1. In dữ liệu thông tin sv')
    print('2. Thêm sv mới')
    print('3. Cập nhật thông tin sv qua mã sv')
    print('4. Xoá sv khỏi danh sách')
    print('5. Tìm danh sách sv rớt môn qua tên môn')
    print('6. Tính điểm tb từng môn')
    tac_vu = input('Chọn 1 tác vụ tương ứng: ')

    if tac_vu == '1':
        noi_dung_file = read_file(duong_dan)
        print_file(noi_dung_file)
    elif tac_vu == '2':
        noi_dung_file = read_file(duong_dan)
        noi_dung_moi = add_account(noi_dung_file)
        luu = input('Nhập y hoặc Y để lưu thay đổi: ')
        if luu == 'y' or luu == 'Y': 
            update_student(duong_dan, noi_dung_moi)
            print('Lưu thành công') 
            
    elif tac_vu == '3':
        noi_dung_file = read_file(duong_dan)
        update_student(noi_dung_file)
        write_file=(duong_dan, noi_dung_file)
        print('Lưu thành công!')
    elif tac_vu == '4':
        noi_dung_file = read_file(duong_dan)
        delete_student(noi_dung_file)
        write_file(duong_dan, noi_dung_file)
        print('Lưu thành công!')
    elif tac_vu == '5':
        noi_dung_file = read_file(duong_dan)
        ket_qua = tim_kiem(noi_dung_file)
        if len(ket_qua) > 1:
            print('Có', len(ket_qua) - 1, 'kết quả được tìm thấy')
            print_file(ket_qua)
        else:
            print('Không tìm thấy dữ liệu')
    elif tac_vu == '6':
        noi_dung_file = read_file(duong_dan)
        set_ma_mon = set()
        for dong in noi_dung_file[1:]:
            set_ma_mon.add(dong[2])
        sort_set_ma_mon = sorted(set_ma_mon)
        print('{:15}{:15}{:15}{:15}'.format('Mã môn', 'Tổng điểm', 'SLSV', 'ĐTB'))
        for ma_mon in sort_set_ma_mon:
            diem_trung_binh(ma_mon, noi_dung_file)