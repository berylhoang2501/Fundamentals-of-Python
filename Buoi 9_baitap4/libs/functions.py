import csv
from datetime import datetime

def read_file(_path):
    f=open(_path,'r',encoding='utf-8')
    content=[]
    for row in csv.reader(f):
        content.append(row)
    f.close()
    return content
def print_file(content):
    for row in content:
        print('{:15}{:25}{:15}{:15}{:10}{:15}{:30}'.format(row[0],row[1],row[2],row[3],row[4],row[5],row[6]))
    return

def write_file(_path,content):
    f=open(_path,'w',encoding='utf-8',newline='')
    csv.writer(f).writerow(content)
    f.close()
    return

def tim_max(content):
    result=[]
    tieu_de=content.pop(0)
    max=0
    for row in content:
        if max<int(row[2]):
            max=int(row[2])
            result=[row]
    result.insert(0,tieu_de)
    return result
        
#phải luôn return content 
#w ghi đè nội dung xuống file (nội dung mới sẽ luôn luôn thay thế nội dung cũ)
#phải nhận định được lúc nào cần dùng w, lúc nào cần dùng a
#writer: thông báo cho ctrinh biết sẽ lưu
#write rows: lưu nhiều dòng
#có liên quan tới dữ liệu cũ thì dùng vòng lặp for