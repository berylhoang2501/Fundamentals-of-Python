try:
    a=float(input('Nhập số bị chia: '))
    b=float(input('Nhập số chia: '))
    thuong=a/b
except ValueError as er1:
    print('Lỗi giá trị: ',er1)
except ZeroDivisionError as er2:
    print('Lỗi chia cho số 0: ',er2)
else:
    print('Thương: ',thuong)