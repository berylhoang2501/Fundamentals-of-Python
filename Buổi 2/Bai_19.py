
loai_xe=input('Chọn xe 4 chỗ hoặc xe 7 chỗ: ')
if loai_xe!='4' and loai_xe!='7':
    print('Chọn loại xe không đúng')
else:
    so_km = float(input('Nhập số km đã di chuyển: '))
    thoi_gian_cho=int(input('Nhập thời gian chờ: '))
    if loai_xe==4:
        if 0<so_km<=0.5:
            tien_di_chuyen=11000
        elif 0.5<so_km<=30:
            tien_di_chuyen=11000+(so_km-0.5)*176000
        else:
            tien_di_chuyen=11000+29.5*17600+(so_km-30)*145000

    else:
        if 0<so_km<=0.5:
            tien_di_chuyen=12000
        elif 0.5<so_km<=30:
            tien_di_chuyen=12000+(so_km-0.5)*196000
        else:
            tien_di_chuyen=12000+29.5*19600+(so_km-30)*17100
        tien_cho=0
        if thoi_gian_cho>5:
            tien_cho=(thoi_gian_cho-5)*750
        print('Tiền chờ: {:,}'.format(tien_cho))
        print('Tiền di chuyển: {:,}'.format(tien_di_chuyen))
        print('Tiền cước: {:,} + {:,} = {:,}'.format(tien_di_chuyen,tien_cho,tien_di_chuyen+tien_cho))
            
        
        
        
#     loai_xe=int(input('Nhập loại xe 4 chỗ hoặc 7 chỗ: '))

# if loai_xe == 4:
#     if so_km <= 0.5:
#         tien_di_chuyen = 11000
#     if so_km <= 31 and so_km > 0.5:
#         tien_di_chuyen = ((so_km - 0.5) * 15300 + 11000)
#     if so_km > 31:
#             tien_di_chuyen = (((so_km - 31) * 12100) + (30.2 * 15300 + 11000))
                     
# if loai_xe == 7:
#     if so_km <= 0.8:
#         tien_di_chuyen = 12000
#     if so_km <= 31 and so_km > 0.5:
#         tien_di_chuyen = ((so_km - 0.8) * 16100 + 12000)
#     if so_km > 31:
#         tien_di_chuyen = (((so_km - 31) * 13800) + (30.2 * 16100 + 12000))

        
# tgian_cho = float(input("Nhap thoi gian cho: "))
# if tgian_cho > 5: 
#     tien_cho = ((tgian_cho -5) * 750)
# else: tien_cho = 0 

# print ('Tong tien di chuyen = {:,}'.format(tien_di_chuyen + tien_cho))

   