list_so=[0,9,-7,54,28,38,29,89,65,78,27]

#Vai trò 1
list_1=[x+2 for x in list_so]
print('List sau khi tăng các phần tử lên 2 đơn vị: ',list_1)

#Vai trò 2
list_2=[x for x in list_so if x<0]
print('List các số âm: ',list_2)

#Vai trò 3
list_3=[x if x>=0 else 0 for x in list_so]
print('List thay thế các số âm bởi số 0: ',list_3)