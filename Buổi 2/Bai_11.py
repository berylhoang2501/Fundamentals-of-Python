'''
Tuần 1 - Bài 11:
Viết chương trình nhập vào 4 số a,b,c,d. 
Tìm và in ra số lớn nhất và số bé nhất trong 4 số vừa nhập.
'''

a,b,c,d=eval(input('Nhập vào 4 số a,b,c,d: '))
lon_nhat = max(a,b,c,d)
nho_nhat = min(a,b,c,d)

print('Giá trị lớn nhất là: ', lon_nhat)
print('Giá trị nhỏ nhất là: ', nho_nhat)