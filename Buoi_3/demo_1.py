while True:
    loai_xe=input('Nhập loại xe: ')
    if loai_xe=='4' or loai_xe=='7':
        break
    else: 
        print('Loại xe chỉ có thể là 4 chỗ hoặc 7 chỗ')
    
#True là điều kiện giả, điều kiện nằm ở If sẽ giúp thoát khỏi vòng lặp
#Áp dụng đối với vòng lặp while không biết trước số lần lặp (nguyên nhân 
# là không biết khi nào người dùng sẽ nhập vô số đúng)