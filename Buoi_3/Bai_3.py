# Tuần 2 - Bài 3: Nhập vào một số nguyên n (n>0), tính các biểu thức sau đây:
# A = tổng các số lẻ nhỏ hơn hay bằng n. 
# C = tích các số từ 1 đến n
# D = tích các số chia hết cho 3 nhỏ hơn hay bằng n

while True:
    n=int(input('Nhập 1 số để tính toán: '))
    if n>=3:
        break
    else: 
        print('Cần nhập 1 số >=3')
        
tongcacso_le=0 
str_tong_le='A='

for i in range(1,n+1,2): #start,stop,step
    tongcacso_le+=i
    str_tong_le+=str(i)+'+' #phép ghép chuỗi
ket_qua=str_tong_le.rstrip('+')+'='
print(ket_qua, tongcacso_le)

#rstrip: loại bỏ các khoảng trắng (hoặc các ký tự không cần thiết khác) ở cuối chuỗi.
# B = tổng các số chẵn nhỏ hơn hay bằng n

while True:
    n=int(input('Nhập 1 số để tính toán: '))
    if n>=2:
        break
    else: 
        print('Cần nhập 1 số >=2')
        
tongcacso_chan=0
str_tong_chan='B='

for i in range(0,n+1,2):
    tongcacso_chan+=i
    str_tong_chan+=str(i)+'+'
ket_qua=str_tong_chan.rstrip('+')+'='
print(ket_qua, tongcacso_chan)

# C = tích các số từ 1 đến n

while True:
    n=int(input('Nhập 1 số để tính toán: '))
    if n>=1:
        break
    else: 
        print('Cần nhập 1 số >=1')
        
tichcacso=1
str_tich='C='

for i in range(1,n+1,1):
    tichcacso+=i
    str_tich+=str(i)+'*'
ket_qua=str_tich.rstrip('*')+'='
print(ket_qua, tichcacso)

# D = tích các số chia hết cho 3 nhỏ hơn hay bằng n

while True:
    n=int(input('Nhập 1 số để tính toán: '))
    if n>=3:
        break
    else: 
        print('Cần nhập 1 số >=3')
        
tichcacso_chiahet3=1
str_tichchiahet='D='

for i in range(3,n+1,3):
    tichcacso_chiahet3*=i
    str_tichchiahet+=str(i)+'*'
ket_qua=str_tichchiahet.rstrip('*')+'='
print(ket_qua, tichcacso_chiahet3)