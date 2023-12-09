so_1=float(input('Nhập số thứ nhất: '))
so_2=float(input('Nhập số thứ hai; '))

print(str(so_1) + "+" + str(so_2) + "=" + str(so_1+so_2))

#Cách 1
print('Tổng: ', so_1+so_2)
print('Hiệu: ', so_1-so_2)
print('Tích: ', so_1*so_2)
print('Thương: ', so_1/so_2)

#Cách 2
print('Tổng: %.1f'%(so_1+so_2))
print('Hiệu: %.1f'%(so_1-so_2))
print('Tích: %.1f'%(so_1*so_2))
print('Thương: %.1f'%(so_1/so_2))

#Cách 3
# dấu : thông báo sắp có format phía sau
# .1f là lấy 1 chữ số thập phân
print('{:.1f} + {:.1f} = {:.1f}'.format(so_1,so_2,so_1+so_2))
print('{:.1f} - {:.1f} = {:.1f}'.format(so_1,so_2,so_1-so_2))
print('{:.1f} * {:.1f} = {:.1f}'.format(so_1,so_2,so_1*so_2))
print('{:.1f} / {:.1f} = {:.1f}'.format(so_1,so_2,so_1/so_2))
    