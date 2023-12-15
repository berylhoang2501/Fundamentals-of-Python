#Nhập 2 số nguyên x và y. Viết chương trình tính tổng bình phương các 
# số từ x đến y.

while True:
    x,y=eval(input('Nhập khoảng để tính tổng: '))
    if x<y:
        break
    else: 
        print('Phải nhập số thứ 1<số thứ 2')

tong=0
for i in range(x,y+1):
    tong+=i**2
    
print('Tổng bình phương từ {} đên {} là {}'.format(x,y,tong))

#y+1 trong range() để bao gồm cả giá trị của y trong phạm vi tính toán.
#lý do: nếu không sử dụng +1 thì ngoặc ) sẽ không lấy giá trị cuối 

        