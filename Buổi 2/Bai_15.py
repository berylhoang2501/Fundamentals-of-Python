'''
Viết chương trình tính tiền mua hàng cho khách hàng, 
biết nếu thành tiền trên 130.000đ sẽ được giảm giá 10%. 
(Người dùng nhập vào tên sản phẩm, số lượng và đơn giá.
'''

ten_sp = input('Nhập tên sản phẩm: ')
so_luong = int(input('Nhập số lượng: '))
don_gia = int(input('Nhập giá tiền: '))
khuyen_mai=0
thanh_tien = so_luong * don_gia  
thanh_tien_km = 0

if thanh_tien > 130000:
    khuyen_mai=int(thanh_tien*0.1)
print('Thành tiền: {:,} - {:,} = {:,} VNĐ'.format(thanh_tien, khuyen_mai, thanh_tien-khuyen_mai))
#     thanh_tien_km = thanh_tien * 0.9
#     # thanh_tien *= 0.9 
# else:
#     thanh_tien_km=thanh_tien
# print('Tổng số tiền mua hàng trc khi km là: {:,}'.format(thanh_tien))
# print('Tổng số tiền mua hàng sau khi km là: {:,}'.format(thanh_tien_km))
# print('Tổng số tiền mua hàng là: {:,}'.format(thanh_tien))

