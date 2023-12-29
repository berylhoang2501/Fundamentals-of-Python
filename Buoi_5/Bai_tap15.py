# Viết chương trình nhập vào 1 năm dương lịch, xuất ra màn hình tên 
# của năm âm lịch tương ứng. Quy tắc xử lý: Can là năm dương lịch chia 
# lấy dư cho 10 Chi là năm dương lịch chia lấy dư cho 12
'''
import calendar
str_year=input('Nhập năm cần kiểm tra: ')
tuple_can="Canh","Tân","Nhâm","Quý","Giáp","Ất","Bính","Đinh","Mậu","Kỷ"
can_index=(str_year%10)
tuple_chi="Thân","Dậu","Tuất","Hợi","Tý","Sửu","Dần","Mão","Thìn","Tị","Ngọ","Mùi"
print(str_year,'là ',tuple_can,tuple_chi)
'''

tuple_can="Canh","Tân","Nhâm","Quý","Giáp","Ất","Bính","Đinh","Mậu","Kỷ"
tuple_chi="Thân","Dậu","Tuất","Hợi","Tý","Sửu","Dần","Mão","Thìn","Tị","Ngọ","Mùi"
while True: 
    nam_duong_lich=int(input('Nhập năm dương lịch cần kiểm tra: '))
    if nam_duong_lich>0:
        break
can=tuple_can[nam_duong_lich%10]
chi=tuple_chi[nam_duong_lich%12]
nam_am_lich=can+' '+chi #phép cộng chuỗi
print(nam_duong_lich,'là năm',nam_am_lich)
    