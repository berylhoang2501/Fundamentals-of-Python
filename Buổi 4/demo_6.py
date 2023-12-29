#Nhập dữ liệu đến khi muốn dừng, không giới hạn số lượng phần tử

list_so=[]
while True:
    x=int(input('Nhập giá trị phần tử cho list: '))
    list_so.append(x)
    tiep_tuc=input('Nhập y hoặc Y để tiếp tục nhập liệu: ')
    if tiep_tuc!='y' and tiep_tuc!='Y':
        break
print('List các số vừa nhập: ',list_so)