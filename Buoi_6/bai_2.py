# Viết chương trình nhập vào 2 số a và b, kiểm tra xem 2 số đó có 
# phải là 2 số thân thiết hay không?  (biết 2 số nguyên dương a và b  
# được gọi là 2 số thân thiết khi và chỉ khi tổng các ước của số a 
# (không kể chính nó) bằng số b và ngược lại).

def tim_uoc(so):
    list_uoc=[]
    for i in range (1,so):
        if so%i==0:
            list_uoc.append(i)
    return list_uoc

while True:
    so1,so2=eval(input('Nhập 2 số để kiểm tra: '))
    if so1>0 and so2>0:
        break
uoc_so1=tim_uoc(so1)
print('Các ước của {} là {}'.format(so1,str(uoc_so1)))
uoc_so2=tim_uoc(so2)
print('Các ước của {} là {}'.format(so2,str(uoc_so2)))
if sum(uoc_so1)==so2 and sum(uoc_so2)==so1:
    print('{} và {} là 2 số thân thiết'.format(so1,so2))
else: 
    print('{} và {} không phải là 2 số thân thiết'.format(so1,so2))
    
    