# Viết chương trình quản lý danh bạ điện thoại như sau:
# 1. Người dùng chọn chức năng 1: xem danh bạ điện thoại (in ra 2 cột gồm sđt và tên)
# 2. Người dùng chọn chức năng 2: cập nhật lại tên thông qua số điện thoại
# 3. Người dùng chọn chức năng 3: thêm mới số điện thoại vào danh bạ
# 4. Người dùng chọn chức năng 4: xóa liên hệ ra khỏi danh bạ 
# 5. Người dùng tìm kiếm số điện thoại thông qua tên
# 6. Nếu người dùng chọn các chức năng khác 4 chức năng trên thì thông báo tác vu sai và thoát khỏi chương trình.

danh_ba={ '0989741258':'Johnny','0903852147':'Katherine','0903712712':'Johnny'}
while True:
    print('CT QUẢN LÝ DANH BẠ ĐIỆN THOẠI')
    print('1. Xem danh bạ')
    print('2. Cập nhật danh bạ')
    print('3. Thêm liên hệ mới')
    print('4. Xóa liên hệ')
    print('5. Tìm kiếm liên hệ thông qua tên')
    tac_vu=input('Chọn 1 trong 4 tác vụ tương ứng: ')
    if tac_vu=='1':
        print('{:25}{:25}'.format('SĐT','Tên'))
        for k,v in danh_ba.items():
            print('{:25}{:25}'.format(k,v))
            
    elif tac_vu=='2':
        sdt=input('Nhập sđt cần cập nhật tên: ')
        for k,v in danh_ba.items():
            if sdt==k:
                ten=input('Nhập tên mới cần lưu: ')
                danh_ba[k]=ten #câu lệnh lưu
                print('Cập nhật thành công')
                break
        else: 
            print('SĐT chưa tồn tại, vui lòng chọn chức năng thêm mới') 
        
        '''
        if sdt in danh_ba:
            ten=input('Nhập tên mới cần lưu: ')
            danh_ba[sdt]=ten #câu lệnh cập nhật
            print('Cập nhật thành công')
        else:
            print('SĐT chưa tồn tại, vui lòng chọn chức năng thêm mới')       
''' 
            
    elif tac_vu=='3':
        sdt=input('Nhập sđt mới cần lưu: ')
        if sdt not in danh_ba:
            ten=input('Nhập tên cần lưu: ')
            danh_ba[sdt]=ten #câu lệnh thêm mới
            print('Thêm mới thành cộng')
        else:
            print('SĐT đã tồn tại, vui lòng chọn chức năng cập nhật')
            
    elif tac_vu=='4':
        sdt=input('Nhập sdt cần xoá: ')
        if sdt in danh_ba:
            del(danh_ba[sdt]) #câu lệnh xoá
            print('Đã xoá thành công')
        else: 
            print('Không thể xoá do sđt không tồn tại')
            
    elif tac_vu=='5':
        ten=input('Nhập tên cần tìm: ')
        ket_qua={}
        for k,v in danh_ba.items():
            if ten==v:
                ket_qua[k]=v
        print('Có',len(ket_qua),'được tìm thấy')
        if len(ket_qua)>0:
            print('{:25}{:25}'.format('SĐT','Tên'))
            for k,v in danh_ba.items():
                print('{:25}{:25}'.format(k,v))
        
    else:
        break 
    
    # :25 chỉ định độ rộng tối thiểu của môi trường được hiển thị 
    # .items() sẽ trả ra 1 cặp giá trị key và value