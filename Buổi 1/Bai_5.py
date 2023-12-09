lai_suat_nam=float(input('Nhập lãi suất năm: '))
so_tien_gui=int(input('Nhập số tiền gửi: '))
so_thang=int(input('Nhập số tháng đã gửi: '))

# /100 để đưa về phần trăm rồi / tiếp cho 12 tháng
lai_suat_thang=(lai_suat_nam/100)/12
tien_lai=int(so_tien_gui*so_thang*lai_suat_thang)

print('Tiền lãi sau {} tháng là: {:,} VNĐ'.format(so_thang,tien_lai))
print('Tiền gốc + tiền lãi = {:,} + {:,} = {:,} VNĐ'.format(so_tien_gui,tien_lai,so_tien_gui+tien_lai))
