#Viết chương trình kiểm tra số nguyên học vào là số chẳn hay số lẻ
so=int(input('Nhập 1 số để kiểm tra: '))
if so%2==0:
    print(so,'là số chẵn')
else:
    print(so,'là số lẻ')
    