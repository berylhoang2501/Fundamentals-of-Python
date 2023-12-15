# Viết chương trình cho phép người dùng nhập vào list số lst_int gồm 
# các phần tử có giá trị tùy ý (nhưng không vượt quá 0-99). 
# Máy tính sẽ phát sinh một con số may mắn bất kì: lucky_number
# trong phạm vi từ  0- 99; Nếu lucky_number có trong lst_int thì in ra:
# "Chúc mừng, bạn đã trúng thưởng!" Nếu lucky_number không có trong lst_int thì in ra: "Chúc bạn may mắn lần sau"
'''
import random
while True:
    n=int(input('Nhập list số tuỳ ý: '))
    if n>0:
        break
list_ngau_nhien=[ ]
for i in range(0,n):
    x=random.randint(0,100)
    list_ngau_nhien.append(n)
print('List các số phát sinh ngẫu nhiên: ',list_ngau_nhien)

lucky_number = random.randint(0, 99)
print('Số may mắn là: {}'.format(lucky_number))

if lucky_number in list_ngau_nhien:
    print("Chúc mừng, bạn đã trúng thưởng!")
else:
    print("Chúc bạn may mắn lần sau")
'''

import random
lucky_number=random.randint(0,100)
so_luot=3
list_so=[]
while so_luot>0:
    x=int(input('Nhập số may mắn của bạn: '))
    if 0<=x<100:
        list_so.append(x)
    else:
        print('Giá trị không hợp lệ')
    so_luot-=1
    print('Bạn còn: ',so_luot,'lượt thứ')
print('Số may mắn: ',lucky_number)
print('Những con số may mắn bạn đã thử: ',list_so)
if lucky_number  in list_so:
    print('Chúc mừng bạn đã trúng thưởng')
else:
    print('Chúc may mắn lần sau!')


    
   
               