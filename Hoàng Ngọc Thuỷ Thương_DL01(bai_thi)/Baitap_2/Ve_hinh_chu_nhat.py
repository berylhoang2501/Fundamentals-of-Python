while True:
    dai = int(input("Nhập chiều dài của hình chữ nhật: "))
    rong = int(input("Nhập chiều rộng của hình chữ nhật: "))
    ky_tu = input("Nhập ký tự để vẽ hình chữ nhật: ")

    for i in range(rong):
        for j in range(dai):
            print(ky_tu, end=' ')
        print()