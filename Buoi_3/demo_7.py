#kiểm ra xem câu nhập vaò co kí tự a hay A không
cau=input('Nhập 1 câu: ')
for ki_tu in cau:
    if ki_tu=='a' or ki_tu=='A':
        print('Trong câu có tồn tại kí tự a hay A')
        break #chỉ có tác dụng dừng vòng lặp
else: 
    print('Không có kí tự a hay A trong câu')
    
# câu lệnh sau else chỉ phát huy tác dụng khi break vô dụng (giả thuyết đặt ra trên Break không đúng)