# Viết chương trình theo dạng module thực hiện các chức năng sau:
# 1. In dữ liệu về thông tin sinh viên lưu trên file
# 2. Thêm sinh viên mới (mã sinh viên không trùng nhau)
# 3. Cập nhật thông tin sinh viên thông qua mã sinh viên
# 4. Xóa sinh viên ra khỏi danh sách
# 5. Tìm kiếm danh sách các bạn sinh viên bị rớt môn thông qua tên môn (kết quả <5 là rớt)
# 6. Tính điểm trung bình cho từng môn học.

import csv

def read_file(duong_dan):
    f=open(duong_dan,'r',encoding='utf-8')
    content=[]
    for row in csv.reader(f):
        content.append(row)
    f.close()
    return content
def print_file(content):
    for row in content:
        print('{:20}{:25}{:15}{:20}{:20}{:20}'.format(row[0], row[1], row[2], row[3], row[4], row[5]))

def add_account(content):
    new_id=[]
    existing_id=[]
    for row in content:
        existing_id.append(row[0])
    new_id=input('Nhập MSSV mới: ')
    if new_id not in existing_id:
        ten=input('Nhập tên: ')
        ma_mon=input('Nhập mã môn học: ')
        ten_mon=input('Nhập tên môn học: ')
        diem=input('Nhập điểm: ')
        content.append([new_id,ten,ma_mon,ten_mon,diem])
        print('Thêm sinh viên mới thành công!')
    else:
        print('Mã sinh viên đã tồn tại, vui lòng chọn chức năng cập nhật tài khoản')
    return content

def update_student(content):
    ma_sv = input('Nhập mã sinh viên cần cập nhật thông tin: ')
    for row in content:
        if ma_sv == row[0]:
            print('Cập nhật thông tin thành công!')
            break
    else:
        print('Không tìm thấy sinh viên có mã số này!')
    with open(__file__, mode='a+', newline='', encoding='utf-8') as file:
        writer = csv.writer(file)
     
def delete_student(content):
    ma_sv = input('Nhập mã sinh viên cần xoá: ')
    for row in content:
        if ma_sv == row[0]:
            content.remove(row)
            print('Xoá sinh viên thành công!')
            break
    else:
        print('Không tìm thấy sinh viên có mã số này!')
    return content

def tim_kiem(content):
    result=[]
    header=content[0]
    result.append(header)
    ten_mon=input('Nhập tên môn học cần tìm sinh viên rớt: ')
    for row in content[1:]:
        if ten_mon==row[3] and float(row[4])<5:
            result.append(row)
    return result

def diem_trung_binh(ma_mon,content):
    #result=[]
    tong_diem=0
    so_luong+=1
    for row in content:
        if ma_mon==row[2]:
            so_luong+=1
            tong_diem+=float(row[4])
            #result.append(row)
    dtb=tong_diem/so_luong
    print('{:15}{:15}{:15}{:15}'.format(ma_mon,str(tong_diem),str(so_luong),str(dtb)))
    
    

