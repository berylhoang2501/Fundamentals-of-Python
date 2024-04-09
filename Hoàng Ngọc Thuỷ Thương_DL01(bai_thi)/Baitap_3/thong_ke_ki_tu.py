chuoi_input = input("Nhập một chuỗi để xử lý: ")
chuoi_input = chuoi_input.replace(" ", "")
tan_so = {}

# Stats
for ky_tu in chuoi_input:
    if ky_tu in tan_so:
        tan_so[ky_tu] += 1
    else:
        tan_so[ky_tu] = 1

print("Kí tự   Tần số")
for ky_tu, so_lan in tan_so.items():
    print("{}      {}".format(ky_tu, so_lan))