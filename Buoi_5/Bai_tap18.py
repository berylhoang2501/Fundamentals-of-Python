# Viết chương trình nhập vào một chuỗi gồm nhiều từ, loại bỏ các từ 
# trùng nhau và sắp xếp chúng theo thứ tự alphabet. Cho biết sau khi 
# loại bỏ các từ trùng nhau, chuỗi gồm bao nhiêu từ và bao nhiêu kí tự.

str_sentence=input('Nhập câu cần xử lý: ')
list_word=str_sentence.split()
set_word=set(list_word) #loại bỏ các từ trùng nhau
sort_set_word=sorted(set_word)
print('Các từ sau khi loại bỏ trùng nhau và sắp xếp: ',sort_set_word)
num_word=len(sort_set_word)
num_char = 0
for word in sort_set_word:
    num_char += len(word)
print('Số từ: ',num_word)
print('Số kí tự: ',num_char)