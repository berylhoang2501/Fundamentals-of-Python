def tinh_dtb(hk1,hk2):
    assert(hk1>0 and hk2>0),'Diem TB>0'
    return(hk1+hk2*2)/3
hk1,hk2=eval(input('Nhập điểm của HK1 và HK2: '))
dtb=tinh_dtb(hk1,hk2)
print('DBT cả năm: %1f'%(dtb))