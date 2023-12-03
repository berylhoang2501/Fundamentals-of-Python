# Lệnh nhập lần lượt
hana,tul,set=eval(input('Nhập vào lần lượt số kẹo của 3 đứa trẻ: '))

#Chia lấy phần dư
print('Số kẹo cần huỷ là: ',(hana+tul+set)%3)

#chia lấy phần nguyên
print('Số kẹo mỗi đứa trẻ nhận được: {} viên kẹo'.format((hana+tul+set)//3))