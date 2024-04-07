# Fundamentals-of-Python.
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
**1. Giới thiệu**

**2. Cấu trúc lặp**
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

Vòng lặp for bên ngoài biểu diễn số hàng, vòng lặp for bên trong biểu diễn số cột

+ rstrip: loại bỏ các khoảng trắng (hoặc các ký tự không cần thiết khác) ở cuối chuỗi
+ y+1 trong range(x,y+1) để bao gồm cả giá trị của y trong phạm vi tính toán. Lý do: nếu không sử dụng +1 thì ngoặc ) sẽ không lấy giá trị cuối 
+ end='\t' làm cho các kí tự in ra cách nhau bởi 1 tab, tạo thành bảng cửu chương theo cột
+ print('\n') là in ra một dòng mới, đảm bảo rằng mỗi hàng của bảng cửu chương được in ra sẽ nằm trên một dòng mới

**3. Câu lệnh break, continue và pass**
+ Break dùng khi dừng vòng lặp lại theo 1 điều kiện nhất định, phải dùng kết hợp với If
+ Continue: Bỏ qua 1 điều kiện nào đó để tiếp tục vòng lặp, phải dùng chung với If
+ Pass

**4. Sử dụng else với cấu trúc lặp**

Những câu lệnh sau else chỉ phát huy tác dụng nếu vòng lặp (cả 2 loại vòng lặp) đc chạy 1 cách trọn vẹn (khi lệnh break 
và lệnh continue không phát huy tác dụng)

+ Đối với vòng lặp while: else sẽ được thực hiện khi điều kiện lặp trở thành False
+ Đối với vòng lặp for: else sẽ được thực hiện sau khi for đã duyệt xong danh sách

### Sự khác nhau giữa vòng lặp while và for
+ Cú pháp:

while điều_kiện:       

for phan_tu in tap_hop_du_lieu:

+ while sử dụng điều kiện để kiểm tra và for sử dụng một tập hợp dữ liệu cụ thể để lặp qua.

## 10/12/2023: Buổi học 4: Hàm_Built-in functions
### Hàm xử lí số học (Number)
+ Hàm toán học (import math)
  
math.ceil(x): làm tròn cận trên

math.floor(x): làm tròn cận dưới

max(x1,x2,..,xn): giá trị lớn nhất trong các tham số x

min(x1,x2,..,xn): giá trị nhỏ nhất trong các tham số x

math.pow(x,y): x mủ y

math.sqrt(x): căn bậc 2 của x 

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
+ .joint: nối các đối tượng chuỗi với nhau

### Hàm xử lí thời gian (Datatime)
+ Thư viện time (import time)

Cần import time để sử dụng

Hàm time.sleep(secs): Hàm sẽ delay chương trình theo số giây truyền vào

+ Thư viện datetime (import datetime)

Hàm datetime.date.today(): kết quả trả về ngày hiện tại của hệ thống

Hàm datetime.date(year,month,day): phải nhập vào kiểu dữ liệu int

Hàm datetime.datetime.now(): Kết quả trả về ngày giờ hiện tại của hệ thống

+ Định dạng chuỗi

+ Thư viện calendar (import calendar)

Hàm calendar.weekday(year, month, day): kết quả trả về thứ, ngày, tháng, năm với giá trị số (0 là monday, 1 là tuesday,..)

## 10/12/2023: Buổi học 4: Kiểu dữ liệu danh sách (Sequence)
### Giới thiệu về Sequence
### List
+ [ ], các phần tử trong list cách nhau bởi dấu ,
+ Hàm pop và remove là dùng riêng cho kiểu dữ liệu List, chỉ có hàm del là build-in functions
+ Lệnh .sort(): sắp xếp tăng dần
+ Lệnh .reverse(): sắp xếp giảm 
+ Lệnh .append(): dùng để thêm các phần tử vào 
+ Lệnh .join(): dùng để nối các phần tử trong list lại với nhau
+ Lệnh .pop(): xoá phần tử trong list theo vị trí index
+ Lệnh del
+ Lệnh remove: sử dụng remove để xoá (xoá thông qua giá trị cụ thể), nếu trong chuỗi có 2 giá trị giống nhau thì mặc định xoá phần tử đầu tiên
+ Lệnh .insert(-1,31) #(vị trí, giá trị cần thêm)
+ Lệnh cập nhât lại giá trị list_so[5]=-5
+ Lệnh .lower(): chuyển đổi chuổi nhập vào thành chữ thường
+ .randint(a,b): tạo 1 số nguyên ngẫu nhiên trong khoảng từ a->b và lưu vào biến
+ .append(x): thêm 1 phần tử vào cuối list

#### List comprehension

Vai trò 1: tạo ra list mới bằng cách tác động lên các phần tử trong list cũ

Vai trò 2: lọc theo các phần tử để thoả mãn những điều kiện nhất định

Vai trò 3: thay thế phần tử này bằng phần tử khác nếu không thoả mãn điều kiện (số lượng phần tử được giữ nguyên)

+ Trong vai trò 3: theo sau x là điều kiện pt đc giữ lại, theo sau else là giá trị thay thế


## 16/12/2023: Buổi học 5: Kiểu dữ liệu danh sách (Sequence) (continue)
### Tuple

Dùng cho những dữ liệu cố định, k thể thay đổi (ví dụ: 12 tháng, 7 ngày trong tuần) thì dùng tuple để lưu trữ

Cú pháp: (phan_tu1,phan_tu2)

Tuple có bao nhiêu xài bấy nhiêu, không sử dụng thêm các lệnh thêm, xoá, sửa

### Dictionary
+ key:value , key không thể trùng, value nên cho vào list để dễ quản lý
+ {}
+ một bộ key:value mới được coi là 1 phần tử
+ Giá trị nào không được phép trùng nhau thì tạo thành key, những giá trị còn lại thì chọn làm value
+ value number thì không cần lm gì cả, value string thì đặt trong dấu nháy đơn

### Set (tập hợp)

Mỗi phần tử chỉ xuất hiện 1 lần duy nhất, thứ tự liệt kê không quan trọng 

+ Tác dụng: loại bỏ các phần tử trùng nhau
+ Chỉ gồm value, cú pháp {set1, set_2,..,}
+ Thêm 1 phần tử trong set: add
+ Thêm nhiều phần tử trong set: update
+ Xoá thì dùng lệnh discard, remove: xoá thông qua gía trị (nếu giá trị đó không tồn tại thì hàm remove sẽ báo lỗi ngay)
+ Lệnh .clear (): Xoá giá trị của các phần tử khác với del: xoá ra khỏi bộ nhớ
+ .pop() : lấy phần tử ra khỏi set, lấy random, nếu cố tình truyền giá trị sẽ báo lỗi
+ Sắp xếp phân tử: dùng sorted (built-in function), có thể dùng cho nhiều kiểu dữ liệu khác nhau

#### Các toán tử và phương thức trên set
+ Set Union (phép hơp): đổ chung tất cả các phần tử vô chung
+ Set Intersection (phép giao): lấy phần giống nhau giữa 2 set
+ Set Difference (phép hiệu)L lấy ra các phần tử riêng biệt (thuộc tập hợp này-là tập hợp đứng trc dấu trừ mà không thuộc tập hợp kia)
+ Set Symetric difference (phép bù)

### Các Buil-in functions xử lý Sequence
+ map(): tạo sequences mới dựa trên 1 phương thức và sequence cũ
+ filter(function,sequence: chỉ trả về True và False, True là giữ lại , False là loại bỏ
+ reduce (): thưởng chỉ tác động lên 2 phần tử. inport functools để sử dụng reduce()


## 17/12/2023: Buổi học 6: Hàm - User-defined Functions
### Định nghĩa
### Xây dựng hàm

def tên hàm([  ]) (lưu ý: nguyên tắc đặt tên giống tên biến), nếu như chỉ in dữ liệu thì không cần return, để tính toán thì phải có return

Đa số những bài tập liên quan tới xử lý dãy số thì dùng kiểu dữ liệu list

+ vừa key vừa value thì dùng for
+ làm việc với key không thì dùng if

### Gọi hàm 
### Phạm vi của biến
+ Biến toàn cục, có giá trị trong toàn bộ ctrinh

Muốn sử dụng lại biến toàn cục thì trước đó phải thêm từ khoá global 

+ Biến cục bộ, chỉ có giá trị trong hàm

### Tham số
+ Tham trị (number,str)
+ Tham số (list,tuple,dict,set) nhưng hầu như ko làm việc với tuple. Dict và list sẽ phổ biến nhất
#### Có 4 kiểu tham số
+ Tham số bắt buộc: phải truyền đủ số lượng và đúng thứ tự
+ Tham số từ khoá: phải truyền đủ số lượng, k cần đúng thứ tự. Phải nhớ tham số đó trong hàm đã đc đặt tên là gì
+ Tham số mặc định: đảm bảo cho đoạn code chạy trơn tru, đối với những gía trị hay dùng thì được phép nhập nhanh (ví dụ: đặt số lương 1 ly là tham số mặc định)
+ Tham số không xác định(chưa biết số lượng chính sác): 1 dấu sao là list, 2 dấu sao là dictionary

### Hàm lambda (hàm ẩn danh)
+ Áp dụng cho những hàm chỉ có 1 giá trị trả về và 1 câu lệnh duy nhất
+ Phía sau lambda cho biết có bao nhiêu tham số truyền vào hàm
+ Cú pháp: lambda[argument1,2]

## 23/12/2023: Buổi học 7: Tập tin - Thư mục
### Làm việc với tập tin văn bản
+ tổ chức dưới dạng module
+ utf-8: mã để đọc những loại ngôn ngữ có dấu
+ f.read: 1 lần đọc xong hết nội dung file
+ f.close(): dừng việc đang làm và lưu lại file
+ return content: trả về biến content
### Làm việc với tập tin CSV
### Thư viện OS

btvn số 2 3 4











