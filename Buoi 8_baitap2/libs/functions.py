import csv
from datetime import datetime

def read_file(_path):
    f=open(_path,'r',encoding='utf-8')
    content=[]
    for row in csv.reader(f):
        content.append(row)
    f.close()
    return content

def print_file(content):
    for row in content:
        print('{:15}{:25}{:15}{:15}{:10}{:15}{:30}'.format(row[0],row[1],row[2],row[3],row[4],row[5],row[6]))

def add_account(content):
    list_ma_dinh_danh=[]
    for row in content:
        list_ma_dinh_danh.append(row[0])
    ma_dinh_danh=input('Nhập mã định danh cho tk mới: ')
    if ma_dinh_danh not in list_ma_dinh_danh:
        ten=input('Nhập tên: ')
        username=input('Nhập username: ')
        _pass=input('Nhập password: ')
        gioi_tinh=input('Nhập giới tính: ')
        bo_phan=input('Nhập bộ phận công tác: ')
        ngay_tao=datetime.now()
        content.append([ma_dinh_danh,ten,username,_pass,gioi_tinh,bo_phan,ngay_tao])
        print('Thêm thành công')
    else:
        print('Mã định danh đã tồn tại, vui lòng chọn chức năng cập nhật tài khoản')
    return content

def update_account(content):
    ma_dinh_danh=input('Nhập mã định danh của tk cần cập nhật: ')
    for row in content:
        if ma_dinh_danh==row[0]:
            #Giữ lại thông tin cũ
            ten=row[1]
            username=row[2]
            _pass=row[3]
            gioi_tinh=row[4]
            bo_phan=row[5]
            cap_nhat=input('Nhấn 1 để cập nhật tên: ')
            if cap_nhat=='1':
                ten=input('Nhập tên mới: ')
            cap_nhat=input('Nhấn 1 để cập nhật username: ')
            if cap_nhat=='1':
                username=input('Nhập username mới: ')
            cap_nhat=input('Nhấn 1 để cập nhật password: ')
            if cap_nhat=='1':
                _pass=input('Nhập password mới: ')
            cap_nhat=input('Nhấn 1 để cập nhật giới tính: ')
            if cap_nhat=='1':
                gioi_tinh=input('Nhập giới tính mới: ')
            cap_nhat=input('Nhấn 1 để cập nhật bộ phận làm việc: ')
            if cap_nhat=='1':
                bo_phan=input('Nhập bộ phận làm việc mới: ')
            #Cập nhật thông tin mới cho dòng
            row[1]=ten
            row[2]=username
            row[3]=_pass
            row[4]=gioi_tinh
            row[5]=bo_phan
            row[6]=datetime.now()
            print('Cập nhật thành công')
            break
    else:
        print('Mã định danh chưa tồn tại, vui lòng chọn chức năng thêm mới')
    return content

def delete_account(content):
    ma_dinh_danh=input('Nhập mã định danh của tài khoản cần xoá: ')
    for row in content:
        if ma_dinh_danh==row[0]:
            username=input('Nhập username: ')
            if username==row[2]:
                _pass=input('Nhập password của tài khoản: ')
                if _pass==row[3]:
                    content.remove(row)
                    print('Xoá thành công')
                    break
                else:
                    print('Không thể xoá tài khoản do sai password')
                    break
            else:
                print('Không thể xoá do username bị sai')
                break
    else:
        print('Mã định danh không tồn tại')
    return content

def tim_kiem(content):
    bo_phan=input('Nhập bộ phận làm việc để thống kê: ')
    ket_qua=[]
    for row in content:
        if bo_phan==row[5]:
            ket_qua.append(row)
    return ket_qua

def update_file(_path,content):
    f=open(_path,'w',encoding='utf-8',newline='')
    csv.writer(f).writerows(content)
    f.close()
        
#phải luôn return content 
#w ghi đè nội dung xuống file (nội dung mới sẽ luôn luôn thay thế nội dung cũ)
#phải nhận định được lúc nào cần dùng w, lúc nào cần dùng a
#writer: thông báo cho ctrinh biết sẽ lưu
#write rows: lưu nhiều dòng
#có liên quan tới dữ liệu cũ thì dùng vòng lặp for