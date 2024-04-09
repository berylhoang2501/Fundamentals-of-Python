try:
    a=float(input('Nhập số bị chia: '))
    b=float(input('Nhập số chia: '))
    print('Thương: %.1f'%(a/b))
except ZeroDivisionError as err:
    print('Lỗi chia cho số 0: ',err)
finally:
    print('Tổng: ',a+b)
    print('Hiệu: ',a-b)
    print('Tích: ',a*b)
    