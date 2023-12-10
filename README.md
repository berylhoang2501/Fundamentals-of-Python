# Fundamentals-of-Python
## 2/12/2023: Buổi học 1: Tổng quan về lập trình Python
### Các khái niệm về lập trình
### Giới thiệu về Python
### Môi trường phát triển ứng dụng
### Xây dựng ứng dụng đầu tiên

Visual studio code (cài phiên bản càng mới càng tốt, tick "open with code"), Pycharm, GG collab, Jupyter notebook
phiên bản python 3.12.0 mới nhất, nên cài thấp hơn 1->2 phiên. Cài với quyền admin, chọn all users

+ Lệnh xuất dữ liệu print('  ') hoặc print("   ")

## 2/12/2023: Buổi học 1: Biến và các kiểu dữ liệu
### Giới thiệu về biến (tìm ra bản chất chung của bài toán, cần nhập vào giá trị gì, xuất ra giá trị gì)
### Định danh

Tên không mở đầu bằng số

Không được chứa những kí tự đặt biệt @, #, %

Tên biến không được trùng với các từ khoá trong Python 

Nên đặt tên gọi nhớ giá trị biến lưu trữ 

Nếu k muốn trùng với từ khoá có thể thêm _ phía trc

### Các kiểu dữ liệu cơ bản
+ Kiểu số (number)

Số nguyên (int)

Số thực (float)

+ Luận lý (boolean): chỉ trả giá trị True, False
+ Kiểu chuỗi (str)
+ Một số lưu ý phổ biến:

Chữ: str (không cần nhập str vô câu lệnh vì máy sẽ tự hiểu)

Tiền vnđ luôn luôn sử dụng kiểu dữ liệu int

Chia lấy phần dư: %

Chia lấy phần nguyên: //

dấu : thông báo sắp có format phía sau

{:.1f} là lấy 1 chữ số thập phân

+ Lệnh nhập dữ liệu lần lượt (nhập đồng loạt): a,b,c=eval(input('
+ Hàm len: dùng để kiểm tra chuỗi có bao nhiêu kí tự
+ S[0] in kí tự đầu tiên từ trái sang phải
+ S[-1] in kí tự đầu tiên từ phải sang trái

### Chuyển đổi kiểu dữ liệu
### Chú thích trong python
### Các thao tác nhập/xuất (Input/Output)

## 3/12/2023: Buổi học 2: Toán tử
### Toán tử số học (Arithmetic Operators)
### Toán tử gán (Assignment Operators)
### Toán tử so sánh (Comparision Operators)

đối với phép toán tử so sánh chỉ có thể trả về True hoặc False

### Toán tử logic (Logical Operators)

+ Toán tử "and"

0<x<10 bằng nghĩa x>0 and x<10

Phép "and" chỉ True khi thoả mãn được tất  cả các giả thuyết

+ Toán tử "or"

Phép "or" True khi chỉ cần 1 giả thuyết True

+ Toán tử "not"là phép phủ định
### Toán tử thành phần (Membership Operators) ("in" và "not in")
### Toán tử định danh (Identity Operators) ("is" và "is not")
### Toán tử Bitwise
  
Hệ thập phân:

Hệ nhị phân: chỉ dùng 2 số 0 và 1

### Độ ưu tiên trong toán tử

## 3/12/2023: Buổi học 2: Cấu trúc điều kiện
### Giới thiệu
### Các cấu trúc điều kiện
+ Cấu trúc if:
+ Cấu trúc if_else: dùng trong trường hợp có 2 hướng để giải quyết vấn đề,else trong trường hợp này được hiểu là ngược lại (nếu đk 1 ko đúng)
+ Cấu trúc if_elif_else:
### 1 số lưu ý 

## 9/12/2023: Buổi học 3: Cấu trúc lặp
### Giới thiệu
### Cấu trúc lặp
#### Vòng lặp while

Đảm bảo lặp  đủ số lần (n=10 thì lặp 10 lần)

Phải kèm với câu lệnh để dừng lại vòng lặp 
#### Vòng lặp for

Lặp với số lần biết trc

Duyệt qua từng phần tử trong 1 tập hợp

+ Hàm range (start, stop, step)

Ví dụ: stop là 11 thì chỉ lấy 10, không lấy ngay chỗ 11

Câu lệnh lặp đi lặp lại thì phải được đặt lùi vào 1 tab

Câu lệnh chỉ sử dụng 1 lần thì cân nhắc thứ tự sắp xếp câu lệnh

### Câu lệnh break, continue và pass
+ Break dùng khi dừng vòng lặp lại theo 1 điều kiện nhất định, phải dùng kết hợp với If
+ Continue: Bỏ qua 1 điều kiện nào đó để tiếp tục vòng lặp, phải dùng chung với If
+ Pass

### Sử dụng else với cấu trúc lặp

Những câu lệnh sau else chỉ phát huy tác dụng nếu vòng lặp (cả 2 loại vòng lặp) đc chạy 1 cách trọn vẹn (khi lệnh break 
và lệnh continue không phát huy tác dụng)

+ Đối với vòng lặp while: else sẽ được thực hiện khi điều kiện lặp trở thành False
+ Đối với vòng lặp for: else sẽ được thực hiện sau khi for đã duyệt xong danh sách

## 10/12/2023: Buổi học 4: Hàm_Built-in functions
### Hàm xử lí số học (Number)
+ Hàm toán học (import math)
  
ceil(x) làm tròn cận trên

floor(x) làm tròn cận dưới

+ Hàm xử lý số ngẫu nhiên (import random)

randrange: một số ngẫu nhiên trong khoảng (start, stop, step)

randin: một số ngẫu nhiên trong khoảng từ start đến stop

sample: giúp chúng ta phát sinh đúng số lượng trog phạm vi nhất định

random: phát sinh ngẫu nhiên số thập phân trong phạm vi từ 0->1

### Hàm xử lí chuỗi (String)
+ Count: đếm số lần xuất hiện của ký tự đó
+ Find: tìm vị trí đầu tiên xuất hiện, nếu tìm không thấy thì trả về giá trị -1
+ strip: loại bỏ kí tự chỉ định ở 2 đầu
+ split: tách chuỗi, sau khi tách xong thì từng phần tử sẽ chuyển thành kiểu dữ liệu list

### Hàm xử lí thời gian (Datatime)
+ Thư viện time (import time)

Cần import time để sử dụng

Hàm time.sleep(secs): Hàm sẽ delay chương trình theo số giây truyền vào

+ Thư viện datetime (import datetime)

Hàm datetime.date.today(): kết quả trả về ngày hiện tại của hệ thống

Hàm datetime.date(year,month,day): phải nhập vào kiểu dữ liệu int

+ Định dạng chuỗi

+ Thư viện calendar (import calendar)

## 10/12/2023: Buổi học 4: Kiểu dữ liệu danh sách (Sequence)
### Giới thiệu về Sequence
### List
+ [ ], các phần tử trong list cách nhau bởi dấu ,
### Tuple
### Dictionary
### Set
### Các Buil-in functions xử lý Sequence













