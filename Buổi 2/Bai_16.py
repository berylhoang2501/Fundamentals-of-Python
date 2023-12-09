diem_tb=float(input('Nhập điểm trung bình: '))

if diem_tb>=8.0:
    print('Xếp loại giỏi')
elif diem_tb>=6.5:
    print('Xếp loại khá')
elif diem_tb>=5.0:
    print('Xếp loại trung bình')
elif diem_tb>=3.5:
    print('Xếp loại yếu')
else:
    print('Xếp loại kém')

'''
if diem_tb<3.5:
    print('Xếp loại kém')
elif diem_tb>=3.5 and diem_tb<5.0:
    print('Xếp loại yếu')
elif diem_tb>=5.0 and diem_tb<6.5:
    print('Xếp loại trung bình')
else:
    '''