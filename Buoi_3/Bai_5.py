#Viết chương trình in bảng cửu chương từ 2 đến n (xuất ra theo cột);
#Số được giữ cố định sẽ là vòng lặp lớn bên ngoài
'''
i = int(input('Nhập i: '))
n = int(input('Nhập n: '))

for i in range(1,11):
    for i in range(2,n+1):
        print('{} x {} = {}'.format(i,n,i*n), end='\t')
    print('\n')
'''
    
while True:
    n=int(input('Nhập điểm dừng của bảng cửu chương: '))
    if n>2:
        break
    else:
        print('Nhập điểm dùng >2')
for i in range (1,11):
    for j in range(2,n+1):
        print('{} x {} = {}'.format(j,i,i*j), end='\t')
    print('\n')
    
#end='\t' làm cho các kí tự in ra cách nhau bởi 1 tab, tạo thành bảng cửu chương theo cột
#print('\n') là in ra một dòng mới, đảm bảo rằng mỗi hàng của bảng cửu chương được in ra sẽ nằm trên một dòng mới.