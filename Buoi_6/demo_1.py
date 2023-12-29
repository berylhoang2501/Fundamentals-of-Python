def thanh_toan(ten,gia,so_luong=1):
#thông số mặt định nên được đặt cuối cung
    print('Tên loại đồ uống: ',ten)
    print('Thành tiền {} x {} = {}'.format(gia,so_luong,gia*so_luong))
print('Trường hợp 1: ')
thanh_toan('coffee',45000)
print('Trường hợp 2: ')
thanh_toan('freeze trà xanh',55000,2)