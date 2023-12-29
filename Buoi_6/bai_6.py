# Sử dụng lambda tính chu vi và diện tích của hình chữ nhât;

chu_vi = lambda a, b: 2 * (a + b)
dien_tich = lambda a, b: a * b
chieu_dai = float(input('Nhập chiều dài hình chữ nhật: '))
chieu_rong = float(input('Nhập chiều rộng hình chữ nhật: '))

print('Chu vi của hình chữ nhật là: {}'.format(chu_vi(chieu_dai, chieu_rong)))
print('Diện tích của hình chữ nhật là: {}'.format(dien_tich(chieu_dai, chieu_rong)))