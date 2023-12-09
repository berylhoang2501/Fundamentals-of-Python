'''
Tuần 1 - Bài 10: 
Viết chương trình nhập vào số tiền muốn đổi, đổi ra các số tờ mệnh giá: 
500.000, 200.000, 100.000, 50.000 và số tiền còn thừa;
'''
 
so_tien = int(input("Nhập số tiền muốn đổi: "))

so_to_500k = so_tien // 500000
#so_tien = so_tien - so_to_500k * 500000
so_tien%=500000
#sau khi đổi hết 500k thì còn dư bao nhiêu tiền (chia lấy phần dư để đem xử lí tiếp)

so_to_200k = so_tien // 200000
#so_tien = so_tien - so_to_200k * 200000
so_tien%=200000

so_to_100k = so_tien // 100000
#so_tien = so_tien - so_to_100k * 100000
so_tien%=100000

so_to_50k = so_tien // 50000
#so_tien = so_tien - so_to_50k * 50000
so_tien%=50000

print('Số tờ mệnh giá 500,000: {:d}'.format(so_to_500k))

print('Số tờ mệnh giá 200,000: ', so_to_200k)
print('Số tờ mệnh giá 100,000: ', so_to_100k)
print('Số tờ mệnh giá 50,000: ', so_to_50k)
print('Số tiền còn thừa: {:,d}'.format(so_tien))

#d là kiểu integer(số nguyên)
#f là kiểu float (số thực)