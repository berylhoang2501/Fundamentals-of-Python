from distutils.file_util import write_file
from libs.functions import *
duong_dan='files/Quehuong.txt'
while True:
    print('CHƯƠNG TRÌNH LÀM VIỆC VỚI FILE TXT')
    print('1. Xem nội dung file')
    print('2. Ghi nội dung xuống file')
    print('3. Thống kê file')
    tac_vu=input('Chọn 1 tác vụ tương ứng: ')
    if tac_vu=='1':
        noi_dung_file=read_file(duong_dan)
        print(noi_dung_file)
    elif tac_vu=='2':
        write_file(duong_dan)
    elif tac_vu=='3':
        num_line,num_word,num_char=thong_ke(duong_dan)
        print('Số dòng: ',num_line)
        print('Số từ: ',num_word)
        print('Số kí tự: ',num_char)
    else:
        break