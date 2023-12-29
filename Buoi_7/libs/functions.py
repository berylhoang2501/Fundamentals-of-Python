def read_file(_path):
    f=open(_path,'r',encoding='utf-8') #đọc file bằng tiếng việt
    content=f.read()
    f.close()
    return content

def write_file(_path):
    f=open(_path,'a',encoding='utf-8')
    new_content='\n'
    new_content+=input('Nhập nội dung cần lưu: ')
    f.write(new_content)
    f.close()
    
def thong_ke(_path):
    f=open(_path,'r',encoding='utf-8')
    so_dong,so_tu,so_ki_tu=0,0,0
    for row in f:
        so_dong+=1
        list_word=row.split()
        so_tu+=len(list_word)
        #so_ki_tu+=len(row) tính cả kí tự space
        for word in list_word:
            so_ki_tu+=len(word)
    f.close()
    return so_dong,so_tu,so_ki_tu 
        
    