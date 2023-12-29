#  Xây dựng các hàm:
# - Nhập username và password của tài khoản vào hệ thống (password phải từ 8 kí tự trở lên);
# - Xem danh sách username và password tương ứng;
# - Cập nhật username và password (nhập pass cũ trước khi tạo pass mới);
# - Xóa username và password;
# Xây dựng chương trình chọn và thực hiện chức năng tương ứng từ hàm đã xây dựng;
# Dữ liệu khởi tạo: tai_khoan={'user01':'abc@123'};
def in_du_lieu(du_lieu):
    print('{:15}{:15}'.format('Username','Password'))
    for k,v in du_lieu.items():
        print('{:15}{:15}'.format(k,v))

def check_upper(password):
    for character in password:
        if character.isupper():
            return True
    return False

def check_lower(password):
    for character in password:
        if character.islower():
            return True
    return False

def check_num(password):
    for character in password:
        if character.isdigit():
            return True
    return False

def check_space(password):
    for character in password:
        if character==' ':
            return False
    return True

def check_pass(password):
    if (check_upper(password) and check_lower(password) and check_num(password)
        and check_space(password) and not password.isalnum() and len(password)>=8):
        return True
    return False

def them_tai_khoan(du_lieu):
    username=input('Nhập username cần thêm: ')
    if username not in du_lieu:
        password=input('Nhập password cho tài khoản: ')
        if check_pass(password):
            du_lieu[username]=password
            print('Thêm mới thành công')
        else:
            print('Mật khẩu chưa đủ mạnh, vui lòng thử lại')
    else: 
        print('Username đã tồn tại')

def cap_nhat(du_lieu):
    username=input('Nhập username: ')
    for k,v in du_lieu.items():
        if username==k:
            current_pass=v
            old_pass=input('Nhập password cũ: ')
            if old_pass==current_pass:
                new_pass=input('Nhập pass mới: ')
                if check_pass(new_pass):
                    du_lieu[username]=new_pass
                    print('Cập nhật thành công')
                    break
                else:
                    print('Mật khẩu mới không hợp lệ, vui lòng thử lại')
            else:
                print('Mật khẩu không trùng khớp với mật khẩu hiện tại')
                break
    else:
        print('Username không tồn tại, vui lòng chọn chức năng thêm mới')
            
def xoa_tai_khoan(du_lieu):
    username=input('Nhập username của tài khoản cần xoá: ')
    for k,v in du_lieu.items():
        for k,v in du_lieu.items():
            if username==k:
                password=input('Nhập password của tài khoản: ')
                if password==v:
                    del(du_lieu[username])
                    print('Xoá thành công')
                    break
                else:
                    print('Sai mật khẩu nên không thể thực hiện thao tác')
                    break
        else:
            print('Username chưa tồn tại')
            
tai_khoan = {'user01': 'abc@123'}

while True:
    print('CHƯƠNG TRÌNH QUẢN LÝ TÀI KHOẢN')
    print('1. Xem tài khoản')
    print('2. Thêm tài khoản')
    print('3. Cập nhật tài khoản')
    print('4. Xóa tài khoản')
    tac_vu=input('Chọn 1 tác vụ tương ứng: ')
    if tac_vu=='1':
        in_du_lieu(tai_khoan)
    elif tac_vu=='2':
        them_tai_khoan(tai_khoan)
    elif tac_vu=='3':
        cap_nhat(tai_khoan)
    elif tac_vu=='4':
        xoa_tai_khoan(tai_khoan)
    else:
        break
    

# def nhap_tai_khoan():
#     user_name=input('Nhập tên đăng nhập: ')
#     password=input('Nhập mật khẩu phải từ 8 kí tự trở lên: ')
#     while len(password)<8:
#         print('Mật khẩu phải có ít nhất 8 kí tự')
#         password=input('Mời nhập lại mật khẩu: ')
#     tai_khoan[user_name]=password
#     print('Tài khoản đã được khởi tạo thành công')

# def xem_danh_sach():
#     print('Danh sách tài khoản: ')
#     for username, password in tai_khoan.items():
#         print('Username: {username}, Password: {password}')

# def cap_nhat_tai_khoan():
#     username = input('Nhập tên đăng nhập: ')
#     if username in tai_khoan:
#         old_password = input('Nhập mật khẩu cũ: ')
#         if old_password == tai_khoan[username]:
#             new_password = input("Nhập mật khẩu mới (phải từ 8 ký tự trở lên): ")
#             while len(new_password) < 8:
#                 print('Mật khẩu mới phải có ít nhất 8 ký tự.')
#                 new_password = input('Nhập lại mật khẩu mới: ')
#             tai_khoan[username] = new_password
#             print('Tài khoản đã được cập nhật thành công.')
#         else:
#             print("Mật khẩu cũ không đúng.")
#     else:
#         print("Tài khoản không tồn tại.")

# def xoa_tai_khoan():
#     username = input("Nhập tên đăng nhập: ")
#     if username in tai_khoan:
#         del tai_khoan[username]
#         print('Tài khoản {username} đã được xóa.')
#     else:
#         print('Tài khoản không tồn tại.')

# def chon_chuc_nang():
#     while True:
#         print("\nChọn chức năng:")
#         print("1. Nhập tài khoản mới")
#         print("2. Xem danh sách tài khoản")
#         print("3. Cập nhật tài khoản")
#         print("4. Xóa tài khoản")
#         print("5. Thoát")
#         choice = input("Nhập lựa chọn của bạn (1-5): ")
#         if choice == '1':
#             nhap_tai_khoan()
#         elif choice == '2':
#             xem_danh_sach()
#         elif choice == '3':
#             cap_nhat_tai_khoan()
#         elif choice == '4':
#             xoa_tai_khoan()
#         elif choice == '5':
#             print("Đã thoát chương trình.")
#             break
#         else:
#             print("Lựa chọn không hợp lệ. Vui lòng chọn lại.")

# Chạy chương trình
# chon_chuc_nang()
