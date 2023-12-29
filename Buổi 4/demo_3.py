#Tạo list n số phát sinh ngẫu nhiên từ 0 -> 100 được nhập từ bàn phím 

import random

while True:
    n=int(input('Nhập điểm dừng: '))
    if n>0:
        break
    
list_ngau_nhien=[]
for i in range(0,n):
    x=random.randint(0,100)
    list_ngau_nhien.append(x)
print('List các số phát sinh ngẫu nhiên: ',list_ngau_nhien)