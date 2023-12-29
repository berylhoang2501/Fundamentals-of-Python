#Đề bài: Sắp xếp lại phần tử trong list 

list_so=[0,9,7,54,28,38,29,89,65,78,27]
list_so_copy=list_so.copy()

#xoá phần tử ở vị trí thứ 5, dùng pop thì phải truyền index nếu list rỗng sẽ mặc định xoá kí tự cuối cùng)
gia_tri_xoa=list_so.pop(9)
print('Giá trị đã xoá: ',gia_tri_xoa)
print('List sau khi xoá: ',list_so)

#sử dụng del để xoá
del(list_so[-1])
print('List sau khi xoá phần tử cuối cùng: ',list_so)

#sử dụng remove để xoá (xoá thông qua giá trị cụ thể), nếu trong chuỗi có 2 giá trị giống nhau
# thì mặc định xoá phần tử đầu tiên
list_so.remove(29)
print('List sau khi xoá giá trị 29: ',list_so)

#thêm phần tử có giá trị 31 vào cuối list
list_so.insert(-1,31) #(vị trí, giá trị cần thêm)
print('List sau khi thêm vào phẩn tử 31: ', list_so)

#Cập nhât lại giá trị
list_so[5]=-5
print('List sau khi cập nhật: ',list_so)
print('List số sao chép: ',list_so_copy)
print('Địa chỉ của list gốc: ',id(list_so))
print('Địa chỉ của list sao chép: ',id(list_so_copy)) 
