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
        print('{:10}{:10}{:10}{:10}{:15}{:15}'.format(row[0],row[1],row[2],row[3],row[4],row[5]))
    return

def them_don_hang_moi(danh_sach_don_hang, duong_dan):
    ma_don_hang = len(danh_sach_don_hang) + 1
    tiep_tuc = input('Nhấn y để thêm sản phẩm vào đơn hàng: ')
    while tiep_tuc.lower() == 'y':
        ma_hang = input('Nhập mã hàng: ')
        so_luong = int(input('Nhập số lượng: '))
        don_gia = float(input('Nhập đơn giá: '))
        ngay_mua = datetime.now().strftime('%Y-%m-%d %H:%M:%S')
        thanh_tien = so_luong * don_gia
        don_hang_moi = [ma_don_hang, ma_hang, so_luong, don_gia, thanh_tien, ngay_mua]
        danh_sach_don_hang.append(don_hang_moi)
        tiep_tuc = input('Nhấn y để thêm sản phẩm vào đơn hàng: ')

    with open(duong_dan, mode='a+', newline='', encoding='utf-8') as file:
        writer = csv.writer(file)
        for don_hang in danh_sach_don_hang[len(danh_sach_don_hang) - len(don_hang_moi):]:
            writer.writerow(don_hang)
    
    return danh_sach_don_hang

def thong_ke(data):
    thong_ke = {}
    is_header = True
    for row in data:
        if is_header:
            is_header = False
            continue
        ma_hd = row[0]
        so_luong = int(row[2])
        thanh_tien = float(row[4])

        if ma_hd not in thong_ke:
            thong_ke[ma_hd] = {'tong_so_luong': so_luong, 'tong_thanh_tien': thanh_tien}
        else:
            thong_ke[ma_hd]['tong_so_luong'] += so_luong
            thong_ke[ma_hd]['tong_thanh_tien'] += thanh_tien

    # In thông tin thống kê theo cột Mã đơn, số lượng, tổng tiền
    print("{:<15} {:<15} {:<15}".format("Mã đơn", "Số lượng", "Tổng tiền"))
    for ma_hd, info in thong_ke.items():
        print("{:<15} {:<15} {:<15}".format(ma_hd, info['tong_so_luong'], info['tong_thanh_tien']))