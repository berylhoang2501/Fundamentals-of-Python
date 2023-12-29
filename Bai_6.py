# Viết chương trình tìm ước chung lớn nhất của 2 số a,b nhâp từ bàn phím;

while True:
    a,b=eval(input('Nhập lần lượt số thứ nhất, số thứ hai: '))
    if a>0 and b>0:
        break
    else:
        print('Nhập 2 số >0')
        
temp1,temp2=a,b
while temp1!=temp2:
    if temp1>temp2:
        temp1-=temp2
    else:
        temp2-=temp1
        
print('Vậy ƯCLN của {} và {} là {}'.format(a,b,temp1))