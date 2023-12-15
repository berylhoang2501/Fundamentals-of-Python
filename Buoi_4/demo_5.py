#xử lý list có kiểu dữ liệu khác nhau

list_result=  [['SV01','TOÁN', 8.5],[ 'SV02','TOÁN',7.5],[ 'SV03','VLY',7.8]]
print('{:10}{:10}{:10}'.format('MÃ SV','MÃ MÔN','KẾT QUẢ'))
for result in list_result:
    print('{:10}{:10}{:10}'.format(result[0],result[1],str(result[2])))
    
#mỗi giá trị sẽ được căn lề phải trong một ô có độ dài 10 ký tự. Nếu độ dài của giá trị
# ít hơn 10 ký tự, khoảng trắng sẽ được thêm vào bên trái để đảm bảo độ rộng của trường 
# là 10 ký tự.