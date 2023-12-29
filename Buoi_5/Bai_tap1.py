# Viết chương trình tính BMI của 1 người biết BMI=cân nặng (kg)/chiều cao(m) **2 đồng thời đưa ra các lời khuyên dựa trên BMI vừa tính được biết rằng:
# - BMI<18: Gầy - cần bổ sung thêm chế độ dinh dưỡng;
# -18 <BMI <25: Cân đối - tiếp tục duy trì;
# -BMI >25: Béo - Cần cân bằng dinh dưỡng và tập luyện;

def tinh_bmi(can_nang,chieu_cao):
    bmi=can_nang/chieu_cao**2
    return bmi
def doi_don_vi(chieu_cao_cm):
    chieu_cao_met=chieu_cao_cm/100
    return chieu_cao_met
def loi_khuyen(bmi):
    if 0<bmi<18:
        print('Gầy. Cần cân đối dinh dưỡng')
    elif 18<=bmi<25:
        print('Bình thường. Cần duy trì')
    else:
        print('Béo. Cần tăng cường tập luyện')  
while True: 
    can_nang=float(input('Nhập cân nặng tính bằng kg: '))
    chieu_cao=float(input('Nhập chiều cao tín bằng mét: '))
    if can_nang>0 and chieu_cao>0:
        break
if chieu_cao>3:
    chieu_cao=doi_don_vi(chieu_cao)
cs_bmi=tinh_bmi(can_nang,chieu_cao)
print('Chỉ số BMI={:.1f}'.format(cs_bmi))
loi_khuyen(cs_bmi)

                    
                
      