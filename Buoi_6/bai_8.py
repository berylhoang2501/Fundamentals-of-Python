# Quản lý gói cước di động

#các hàm xử lý
def xem_goi_cuoc(du_lieu):
    print('{:10}{:10}{:10}{:10}'.format('Mã gói','Giá','DL','Thời hạn'))
    for k,v in du_lieu.items():
        print('{:10}{:10}{:10}{:10}'.format(k,str(v[0]),str(v[1]),str(v[2])))
                        
def them_goi_cuoc(du_lieu):
    ma_goi=input('Nhập mã gói mới: ')
    if ma_goi in du_lieu:
        print('Mã gói đã tồn tại, vui lòng chọn chức năng cập nhật')
    else:
        gia=int(input('Nhập giá gói cước: '))
        dung_luong=float(input('Nhập dung lượng: '))
        thoi_han=int(input('Nhập thời hạn: '))
        du_lieu[ma_goi]=[gia,dung_luong,thoi_han] #câu lệnh thêm mới
        print('Thêm gói cước thành công')
        
def cap_nhat_goi(du_lieu):
    ma_goi=input('Nhập mã gói cần cập nhật: ')
    if ma_goi in du_lieu:
        #lưu dữ liệu cũ
        chi_tiet_goi=du_lieu[ma_goi]
        gia=chi_tiet_goi[0]
        dung_luong=chi_tiet_goi[1]
        thoi_hạn=chi_tiet_goi[2]
        lua_chon=input('Nhấn 1 để cập nhật giá: ')
        if lua_chon=='1':
            gia=int(input('Nhập giá mới của gói cược: '))
        lua_chon=input('Nhấn 1 để cập nhật dung lượng: ')
        if lua_chon=='1':
            thoi_hạn=int(input('Nhập thời hạn mới của gói cược: '))
        du_lieu[ma_goi]=[gia,dung_luong,thoi_hạn] #câu lệnh cập nhật
        print('Cập nhật thành công')
    else:
        print('Mã gói cước không tồn tại. Vui lòng chọn chức năng thêm mới')
    
def tinh_dltb(du_lieu):
    print('{:15}{:15}{:15}{:15}'.format('Mã gói','Dung lượng','Thời hạn','DLTB'))
    for k,v in du_lieu.items():
        print('{:15}{:15}{:15}{:15}'.format(k,str(v[1]),str(v[2]),str(v[1]/v[2])))
        
#chương trình chính
goi_cuoc={'D3':[15000,3,3],'DT30':[30000,7,7],'M50':[50000,1.2,30]}
while True:
    print('CT QUẢN LÝ GÓI CƯỢC DI ĐỘNG')
    print('1. Xem gói cược')     
    print('2. Thêm gói cược mới')   
    print('3. Cập nhật gói cược')   
    print('4.  DLBT')   
    tac_vu=input('Chọn 1 tác vụ tương ứng: ')
    if tac_vu=='1':
        xem_goi_cuoc(goi_cuoc)
    elif tac_vu=='2':
        them_goi_cuoc(goi_cuoc)
    elif tac_vu=='3':
        cap_nhat_goi(goi_cuoc)
    elif tac_vu=='4':
        tinh_dltb(goi_cuoc)
    else:
        break