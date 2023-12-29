#Tạo list gồm các số lẻ trong phạm vi 0->n

while True:
    n=int(input('Nhập điểm dừng: '))
    if n>0:
        break
list_so_le=[]
for i in range(1,n+1,2):
    list_so_le.append(i)
print('List các số lẻ: ',list_so_le)