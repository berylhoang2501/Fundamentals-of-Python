# Viết chương trình kiểm tra xem số N có phải là số hoàn hảo hay không? Biết số hoàn hảo là một số nguyên dương mà tổng các ước nguyên dương chính thức của nó bằng chính nó.
# Ví dụ: 6 là số hoàn hảo vì 1+2+3=6 (1,2,3 là các ước)

while True:
    n=int(input('Nhập 1 số để kiểm tra: '))
    if n>0:
        break
        
tong_uoc = 0
str_uoc=' '
for i in range(1,n):
    if n%i==0: #chia hết
        tong_uoc+=i
        str_uoc+=str(i)+'+'
cac_uoc=str_uoc.rstrip('+')+'='
print('Tổng các ước: ')
print(cac_uoc,tong_uoc)
if tong_uoc==n:
    print(n,'là số hoàn hảo')
else: 
    print(n,'không là số hoàn hảo')
    