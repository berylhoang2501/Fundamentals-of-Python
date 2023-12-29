# Viết chương trình từ điển với các chức năng sau:
# 1. Người dùng chọn chức năng 1: xem từ điển (in ra 2 cột gồm từ Anh và nghĩa Việt)
# 2. Người dùng chọn chức năng 2: cập nhật lại nghĩa tiếng Việt (thông qua từ tiếng Anh)
# 3. Người dùng chọn chức năng 3: thêm từ vào từ điển (kiểm tra xem từ này đã tồn tại chưa, nếu tồn tại rồi thì yêu cầu nhập lại 1 từ khác). Lưu ý: một từ có thể có nhiều nghĩa và lưu nghĩa của từ vào list.
# 4. Người dùng chọn chức năng 4: xóa từ ra khỏi từ điển (thông qua từ tiếng Anh, nếu từ không có trong từ điển thì thông báo tên không tồn tại);
# 5. Nếu người dùng chọn các chức năng khác 4 chức năng trên thì thông báo tác vu sai và thoát khỏi chương trình.
# Dữ liệu khởi tạo: tu_dien={'one':['số 1','con số 1'],'father':['cha','bố']}

tu_dien={'one':['số 1','con số 1'],'father':['cha','bố']}

while True:
    print('CT TỪ ĐIỂN')
    print('1. Xem từ điển')
    print('2. Cập nhật lại nghĩa tiếng việt')
    print('3. Thêm từ mới')
    print('4. Xóa từ ra khỏi từ điển')
    chuc_nang=input('Chọn 1 trong 4 chức năng tương ứng: ')
    
    if chuc_nang=='1':
        print('{:15}{:20}'.format('Từ tiếng Anh', 'Nghĩa Việt'))
        for tu, nghia in tu_dien.items():
            print('{:15}{:20}'.format(tu, ', '.join(nghia)))

    elif chuc_nang == '2':
        tu_tieng_anh = input('Nhập từ tiếng Anh cần cập nhật nghĩa: ')
        if tu_tieng_anh in tu_dien:
            nghia=tu_dien[tu_tieng_anh] #lưu các nghĩa cũ trong 1 list
            nghia_moi = input('Nhập nghĩa tiếng Việt mới cách nhau bởi dấu, : ') #nhập nghĩa mới ở dạng string
            list_nghia_moi=nghia_moi.split(', ') #tách và chuyển các nghĩa mới về dạng list
            nghia.extend(list_nghia_moi) #đồng bộ nghĩa cũ và nghĩa mới
            tu_dien[tu_tieng_anh] = nghia
            print('Cập nhật thành công!')
        else:
            print('Từ không tồn tại trong từ điển.')
                 
    elif chuc_nang == '3':
        tu_tieng_anh_moi = input('Nhập từ tiếng Anh mới: ')
        if tu_tieng_anh_moi in tu_dien:
            print('Từ này đã tồn tại trong từ điển.')
        else:
            nghia_moi = input('Nhập nghĩa tiếng Việt cho từ mới: ')
            tu_dien[tu_tieng_anh_moi] = [nghia_moi]
            print('Thêm từ thành công!')

    elif chuc_nang == '4':
        tu_can_xoa = input('Nhập từ tiếng Anh cần xóa: ')
        if tu_can_xoa in tu_dien:
            del tu_dien[tu_can_xoa]
            print('Xóa từ thành công!')
        else:
            print('Từ không tồn tại trong từ điển.')

    else:
        print('Tác vụ không hợp lệ. Hãy chọn từ 1 đến 4.')
    