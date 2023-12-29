# Viết chương trình kiểm tra số n có phải là số nguyên tố (số nguyên tố là số chỉ chia hết cho 1 và chính nó).

while True:
    so=int(input('Nhập 1 số để kiểm tra: '))
    if so>=2:
        break
for i in range(2,so):
    if so%i==0:
        print(so,'không phải là số nguyên tố')
        break
else:
    print(so,'là số nguyên tố')