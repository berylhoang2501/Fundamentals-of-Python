#Tạo list gồm các số chẵn trong phạm vi 0->n

while True:
    n=int(input('Nhập điểm dừng: '))
    if n>0:
        break
list_so_chan=[]
for i in range(0,n+1,2):
    list_so_chan.append(i)
print('List các số chẵn: ',list_so_chan)