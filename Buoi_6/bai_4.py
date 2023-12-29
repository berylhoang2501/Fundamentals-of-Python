# ; Dãy Fibonacci là dãy vô hạn các số tự nhiên bắt đầu bằng hai phần 0 và 1, các phần tử sau đó được
# ; thiết lập theo quy tắc mỗi phần tử luôn bằng tổng hai phần tử trước nó.
# ; Viết chương trình in ra dãy Fibbonacci gồm n số hạng đầu tiên.

def tao_day_fib(n):
    day_so=[0,1]
    for i in range(2,n):
        x=day_so[i-2]+day_so[i-1]
        day_so.append(x)
    return day_so
while True: 
    so_luong=int(input('Nhập số lượng phần tử của dãy Fib: '))
    if so_luong>=2:
        break
day_fib=tao_day_fib(so_luong)
print('Dãy Fib gồm {} phần tử đầu tiên là {}'.format(so_luong,day_fib))

