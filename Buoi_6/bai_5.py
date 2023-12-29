import math

while True: 
    diem_dung=int(input('Nhập điểm dừng của tam giác pascal: '))
    if diem_dung>0:
        break
def tinh_c(n,k):
    return int(math.factorial(n)/(math.factorial(k)*math.factorial(n-k)))
for i in range(0,diem_dung+1):
    for j in range(0,i+1):
        print(tinh_c(i,j),end='\t')
    print('\n')
    
    