def tao_capsocong(n,u0,d):
    list_so=[u0]
    for i in range(1,n):
        x=list_so[i-1]+d
        list_so.append(x)
    return list_so

while True:
    so_luong=int(input('Nhập số lượng phần tử của csc: '))
    if so_luong>0:
        break
cong_sai=int(input('Nhập công sai của csc: '))
bat_dau=int(input('Nhập giá trị của phần tử mở đầu: '))
day_csc=tao_capsocong(so_luong,bat_dau,cong_sai)
print('Dãy csc có {} phần tử là: {}',format(so_luong,str(day_csc)))
                       
'''
u0 = float(input('Nhập số hạng đầu tiên u0: '))
d = float(input('Nhập công sai d: '))
n = float(input('Nhập số lượng số hạng cần xuất ra: '))

result=capsocong(u0,d,n)
print('Số hạng đầu tiên của dãy cấp số cộng là {}'.format(u0))
'''