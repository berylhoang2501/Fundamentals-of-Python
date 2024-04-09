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
        print('{:10}{:20}{:10}{:15}{:10}{:15}{:30}'.format(row[0],row[1],row[2],row[3],row[4],row[5],row[6]))
    return

def write_file(_path,content):
    f=open(_path,'a',encoding='utf-8',newline='')
    csv.writer(f).writerows(content)
    f.close()
    return

def them_don_hang(content):
    don_hang_cuoi=content[-1] #lấy thông tin của đơn hàng cuối cùng
    ma_don=don_hang_cuoi[0] #Lấy mã đơn
    ma_don=int(ma_don)+1
    new_order=[] #Lưu lại tất cả các mặt hàng đã order
    loai_thuc_pham={'1':['Gà rán',45000,'miếng'],
                    '2':['Coca Cola',14000,'chai'],
                    '3':['Khoai tây chip',45000,'gram'],
                    '4':['Xiên que đồng giá',15000,'que']} #lưu thông tin của các mặt hàng đang bán
    while True:
        tiep_tuc=input('Nhấn y để tiếp tục order: ')
        if tiep_tuc=='y':
            chon_tp=input('1. Chọn gà rán, 2. Chọn Cola Cola, 3. Chọn khoai tây chip. 4. Chọn xiên que đồng giá: ')
            if chon_tp=='1':
                thong_tin=loai_thuc_pham['1']
            elif chon_tp=='2':
                thong_tin=loai_thuc_pham['2']    
            elif chon_tp=='3':
                thong_tin=loai_thuc_pham['3']      
            elif chon_tp=='4':
                thong_tin=loai_thuc_pham['4']    
            ten_tp=thong_tin[0]
            gia=thong_tin[1]
            dvt=thong_tin[0]
            gia=thong_tin[1]
            so_luong=int(input('Nhập số lượng: '))
            thanh_tien=gia*so_luong
            ngay_order=datetime.now()
            order_info=[ma_don,ten_tp,so_luong,dvt,gia,thanh_tien,ngay_order] #lưu thông tin của từng mặt hàng 
            new_order.append(order_info)
        else:
            break
    return new_order
        