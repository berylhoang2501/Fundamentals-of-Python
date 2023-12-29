from libs.functions import *
duong_dan='files/madinhdanh.csv'
while True:
    print('CHƯƠNG TRÌNH QUẢN LÝ TÀI KHOẢN')
    print('1. Xem các tk')
    print('2. Thêm tk mới')
    print('3. Cập nhật tk')
    print('4. Xoá tk')
    print('5. Thống kê')   
    tac_vu=input('Chọn 1 tác vụ tương ứng: ')
    if tac_vu=='1':
        noi_dung_file=read_file(duong_dan)
        print_file(noi_dung_file)
    elif tac_vu=='2':
        noi_dung_file=read_file(duong_dan)
        noi_dung_moi=add_account(noi_dung_file)
        luu=input('Nhập y hoặc Y để lưu thay đổi: ')
        if luu=='y' or luu=='Y':
            update_file(duong_dan,noi_dung_moi)
            print('Lưu thành công')
    elif tac_vu=='3':
        noi_dung_file=read_file(duong_dan)
        noi_dung_moi=update_account(noi_dung_file)
        luu=input('Nhập y hoặc Y để lưu thay đổi: ')
        if luu=='y' or luu=='Y':
            update_file(duong_dan,noi_dung_moi)
            print('Lưu thành công')
    elif tac_vu=='4':
        noi_dung_file=read_file(duong_dan)
        noi_dung_moi=delete_account(noi_dung_file)
        luu=input('Nhập y hoặc Y để lưu thay đổi: ')
        if luu=='y' or luu=='Y':
            update_file(duong_dan,noi_dung_moi)
            print('Lưu thành công')
    elif tac_vu=='5':
        noi_dung_file=read_file(duong_dan)
        dong_tieu_de=noi_dung_file.pop(0)
        ket_qua=tim_kiem(noi_dung_file)
        print('Có',len(ket_qua),'Kết quả được tìm thấy')
        if len(ket_qua)>0:
            ket_qua.insert(0,dong_tieu_de)
            print_file(ket_qua)
    else:
        break
