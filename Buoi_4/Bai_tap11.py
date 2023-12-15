#kiểm tra sự tồn tại của phần tử trong list cho trước
# Tìm thú trong vườn thú: - Tạo ra một list tên có các con thú: 
# animal_name; - Nhập vào tên 1 con thú cần tìm: search_name - Trả kết quả có tìm thấy được hay không? Nếu tìm thấy thì tìm thấy mấy lần?

list_name= ['zebra','dog','cat','duck','cat','tiger','bear']
search_name=input('Nhập tên cần tìm: ')
if search_name.lower() in list_name:
    so_lan=list_name.count(search_name.lower())
    print(search_name.lower(),'xuất hiện',so_lan,'lần')
else:
    print('Tên chưa tồn tại trong danh sách lưu trữ')