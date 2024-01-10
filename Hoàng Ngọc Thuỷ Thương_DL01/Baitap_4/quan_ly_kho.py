users={'user01':['Phan Hoàng Hải Đăng','Abcd@123'],
'user02':['Lưu Minh Phúc','Abcd@123'],
'user03':['Đỗ Thái Minh','Abcd@123']}

def in_du_lieu(du_lieu):
    print('{:15}{:20}{:15}'.format('Username', 'Name', 'Password'))
    for k, v in du_lieu.items():
        print('{:15}{:20}{:15}'.format(k, v[0], v[1]))

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
    username = input('Nhập username cần thêm: ')
    if username not in du_lieu:
        name = input('Nhập tên người dùng: ')
        password = input('Nhập password cho tài khoản: ')
        if check_pass(password):
            du_lieu[username] = [name, password]
            print('Thêm mới thành công')
        else:
            print('Mật khẩu chưa đủ mạnh, vui lòng thử lại')
    else: 
        print('Tên đăng nhập không hợp lệ')

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
                    print('Thêm thành công')
                    break
                else:
                    print('Mật khẩu mới không hợp lệ, vui lòng thử lại')
            else:
                print('Mật khẩu không trùng khớp với mật khẩu hiện tại')
                break
    else:
        print('Username không tồn tại, vui lòng chọn chức năng thêm mới')

while True:
    print('CT QUẢN LÝ TÀI KHOẢN')
    print('1. Xem các tài khoản')
    print('2. Thêm một tài khoản')
    tac_vu = input('Chọn 1 tác vụ tương ứng: ')
    if tac_vu == '1':
        in_du_lieu(users)
    elif tac_vu == '2':
        them_tai_khoan(users)
    else:
        break