
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

<img width="662" alt="Ảnh màn hình 2025-03-24 lúc 14 22 27" src="https://github.com/user-attachments/assets/f060f8fd-c77d-4830-b468-828bc9ca3581" />

+ Kiểu số (number)

Số nguyên (int)

Số thực (float)

+ Luận lý (boolean): chỉ trả giá trị True, False
+ Kiểu chuỗi (str). Là một chuỗi ký tự được đặt trong nháy kép (" ") hoặc nháy đơn (* '). vi dụ:  name = "Trung tâm Tin học"
+ Một số lưu ý phổ biến:

Chữ: str (không cần nhập str vô câu lệnh vì máy sẽ tự hiểu). 

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

<img width="565" alt="Ảnh màn hình 2025-03-25 lúc 20 45 57" src="https://github.com/user-attachments/assets/d50226b9-1010-4cb2-b36d-4109f69d7437" />

<img width="576" alt="Ảnh màn hình 2025-03-26 lúc 02 05 28" src="https://github.com/user-attachments/assets/c6e1366f-9e1a-479c-a2ad-bf26bc9d4a9d" />

{:,.0f} -> :, là format Phân cách hàng nghìn

-> .0f là format Phân cách thập phân

lấy range index: [a:b]
ví dụ: print("{} ký tự từ vị trí index {} đến {} là: ".format(cm_bd, ki_tu, ket_thuc), chuoi[cm_bd:ket_thuc])

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

<img width="808" alt="Ảnh màn hình 2025-03-31 lúc 15 12 09" src="https://github.com/user-attachments/assets/78aea1a7-435c-4cd5-9b6f-d926ad5c779c" />

<img width="832" alt="Ảnh màn hình 2025-03-31 lúc 15 13 39" src="https://github.com/user-attachments/assets/17b949e9-8fe1-4112-a690-d53f74d462a3" />

math.ceil(x): làm tròn cận trên

math.floor(x): làm tròn cận dưới

max(x1,x2,..,xn): giá trị lớn nhất trong các tham số x

min(x1,x2,..,xn): giá trị nhỏ nhất trong các tham số x

math.pow(x,y): x mủ y

math.sqrt(x): căn bậc 2 của x 

+ Hàm xử lý số ngẫu nhiên (import random)

<img width="824" alt="Ảnh màn hình 2025-03-31 lúc 15 15 54" src="https://github.com/user-attachments/assets/a091cb27-d36a-436a-a2d3-21cea1733497" />

randrange: một số ngẫu nhiên trong khoảng (start, stop, step)

randin: một số ngẫu nhiên trong khoảng từ start đến stop

sample: giúp chúng ta phát sinh đúng số lượng trog phạm vi nhất định

random: phát sinh ngẫu nhiên số thập phân trong phạm vi từ 0->1

### Hàm xử lí chuỗi (String)
<img width="805" alt="Ảnh màn hình 2025-03-31 lúc 15 16 46" src="https://github.com/user-attachments/assets/a58ce136-eeff-43c4-b94c-82ed266de2c9" />
<img width="801" alt="Ảnh màn hình 2025-03-31 lúc 15 18 30" src="https://github.com/user-attachments/assets/4b9037cb-a942-46ee-93cd-7a3c76d336ab" />
<img width="820" alt="Ảnh màn hình 2025-03-31 lúc 15 20 45" src="https://github.com/user-attachments/assets/422cc8bd-b26e-4a3e-8952-56b73320614d" />
<img width="811" alt="Ảnh màn hình 2025-03-31 lúc 15 22 27" src="https://github.com/user-attachments/assets/e52cd60d-fd48-4731-8b63-013842517845" />
<img width="819" alt="Ảnh màn hình 2025-03-31 lúc 15 23 28" src="https://github.com/user-attachments/assets/c7f88848-88ca-4e4c-84ed-8c117e430fb5" />

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

<img width="777" alt="Ảnh màn hình 2025-03-31 lúc 15 27 46" src="https://github.com/user-attachments/assets/365e14c4-2d76-4661-9356-2efd395ea7ae" />

+ Thư viện calendar (import calendar)

Hàm calendar.weekday(year, month, day): kết quả trả về thứ, ngày, tháng, năm với giá trị số (0 là monday, 1 là tuesday,..)

## 10/12/2023: Buổi học 4: Kiểu dữ liệu danh sách (Sequence)
**1. Giới thiệu về Sequence**

**2. List**
+ [ ], các phần tử trong list cách nhau bởi dấu ,
+ Cập nhật 1 phần tử: ten_list[index] = gia_tri
+ Cập nhật danh sách các phần tử liên tục: list_numbers[1:4] = [20, 40, 60]
+ Duyệt list: for item in ten_list
+ Thêm phần tử vào list tại vị trí index: ten _list.insert(index, phan_tu)
+ Mở rộng list: ten_ list_muon_mo_rong.extend(ten_list) #[1, 2, 3, 4, 5, 6] còn nếu dùng append thì là [1, 2, 3, [4, 5, 6]]
+  Đếm số lần xuất hiện của một phần tử trong list: ten_list. count(phan_tu)
+ Hàm pop và remove là dùng riêng cho kiểu dữ liệu List, chỉ có hàm del là build-in functions
+ Lệnh .sort(): sắp xếp tăng dần
+ Lệnh .reverse(): sắp xếp giảm 
+ Lệnh .append(): dùng để thêm các phần tử vào cuối list
+ Lệnh .join(): dùng để nối các phần tử trong list lại với nhau
+ Lệnh .pop(): xoá phần tử trong list theo vị trí index
+ Lệnh del
+ Lệnh remove: sử dụng remove để xoá (xoá thông qua giá trị cụ thể), nếu trong chuỗi có 2 giá trị giống nhau thì mặc định xoá phần tử đầu tiên
+ Lệnh .insert(-1,31) #(vị trí, giá trị cần thêm)
+ Lệnh cập nhât lại giá trị list_so[5]=-5
+ Lệnh .lower(): chuyển đổi chuổi nhập vào thành chữ thường
+ .randint(a,b): tạo 1 số nguyên ngẫu nhiên trong khoảng từ a->b và lưu vào biến
+ .append(x): thêm 1 phần tử vào cuối list
+ .index(): trả về chỉ số đầu tiên của phần tử mà bạn tìm trong list

#### List comprehension

Vai trò 1: tạo ra list mới bằng cách tác động lên các phần tử trong list cũ

Vai trò 2: lọc theo các phần tử để thoả mãn những điều kiện nhất định

Vai trò 3: thay thế phần tử này bằng phần tử khác nếu không thoả mãn điều kiện (số lượng phần tử được giữ nguyên)

+ Trong vai trò 3: theo sau x là điều kiện pt đc giữ lại, theo sau else là giá trị thay thế


## 16/12/2023: Buổi học 5: Kiểu dữ liệu danh sách (Sequence) (continue)
**3. Tuple**

Dùng cho những dữ liệu cố định, k thể thay đổi (ví dụ: 12 tháng, 7 ngày trong tuần) thì dùng tuple để lưu trữ

Cú pháp: (phan_tu1,phan_tu2)

Tuple có bao nhiêu xài bấy nhiêu, không sử dụng thêm các lệnh thêm, xoá, sửa

+ Có thể không sử dụng () khi tạo tuple

+ Lưu ý: Khi tạo tuple có 1phần tử, cần thêm dấu phẩy (,) vào sau phần ửt đó.

+ Cũng tương tự như các phương thức cơ bản của list nhưng không có phương thức: sort(), reverse(), remove(), pop(), insert(), extend(), append()

+ lấy index

thistuple = (1, 3, 7, 8, 7, 5, 4, 6, 8, 5)

x = thistuple.index(8)

**4. Dictionary**
+ key:value , key không thể trùng, value nên cho vào list để dễ quản lý
+ {}
+ một bộ key:value mới được coi là 1 phần tử
+ Giá trị nào không được phép trùng nhau thì tạo thành key, những giá trị còn lại thì chọn làm value
+ value number thì không cần lm gì cả, value string thì đặt trong dấu nháy đơn

+ Khai báo và gắn gía trị:

<img width="492" alt="Ảnh màn hình 2025-04-04 lúc 00 33 37" src="https://github.com/user-attachments/assets/735560da-978e-4f36-9b82-d43fbe006950" />

+ Tạo dictionary: Sử dụng hàm dict():

![Ảnh màn hình 2025-04-04 lúc 00 35 14](https://github.com/user-attachments/assets/978cc1ff-47a8-4c1c-acd4-2560715161cf)

+ Truy xuất giá trị trong dictionary: Cú pháp: ten_dictionary[key]

+ Cập nhật / thêm mới giá trị vào dictionary. Cú pháp: ten_dictionary[key] = gia_tri

+ Tạo dictionary với danh sách các key từ sequence: ten_dict = dict.fromkeys(seq[,value])

![Ảnh màn hình 2025-04-06 lúc 01 13 08](https://github.com/user-attachments/assets/fce67fb5-cb8f-4525-86f6-ed2e81a94822)

+ for key, value in ten_dictionary.items(): Trả về danh sách các bộ tuple (key, value) của dictionary

![Ảnh màn hình 2025-04-06 lúc 01 15 45](https://github.com/user-attachments/assets/1f161241-afeb-4dd5-834e-73002b4ea50a)

+ ten_dictionary. keys(): Trả về danh sách các key của dictionary

+ ten_dictionary.values(): Trả về danh sách các value của dictionary

+ ten _dictionary_1.update(ten_dictionary_2): Cập nhật các phần tử từ ten_dictionary_2 vào ten_dictionary_1

<img width="290" alt="Ảnh màn hình 2025-04-08 lúc 02 07 59" src="https://github.com/user-attachments/assets/e3850999-a978-4593-b936-d2d324145f44" />

**5. Set (tập hợp)**

Mỗi phần tử chỉ xuất hiện 1 lần duy nhất, thứ tự liệt kê không quan trọng 

Có thể chứa biến thuộc nhiều kiểu dữ liệu khác nhau, nhưng không thể chứa phần ửt có thể thay đổi được như list, set hay dictionary.

Các phần tử trong set không theo thứ tự thêm vào, không sử dụng index.

+ (set1, set_2,., set_n}
+ Tác dụng: loại bỏ các phần tử trùng nhau
+ Chỉ gồm value, cú pháp {set1, set_2,..,}
+ Thêm 1 phần tử trong set: ten_set.add()
+ Thêm nhiều phần tử trong set: ten_set.update()
+ Xoá thì dùng lệnh discard, remove: xoá thông qua gía trị (nếu giá trị đó không tồn tại thì hàm remove sẽ báo lỗi ngay)
+ Lệnh .clear (): Xoá giá trị của các phần tử khác với del: xoá ra khỏi bộ nhớ
+ .pop() : lấy phần tử ra khỏi set, lấy phần tử cuối, lấy random, nếu cố tình truyền giá trị sẽ báo lỗi
+ Sắp xếp phân tử: dùng sorted (built-in function), có thể dùng cho nhiều kiểu dữ liệu khác nhau

#### Các toán tử và phương thức trên set
+ Set Union (phép hơp): đổ chung tất cả các phần tử vô chung .union()
+ Set Intersection (phép giao): lấy phần giống nhau giữa 2 set . intersection()
+ Set Difference (phép hiệu)L lấy ra các phần tử riêng biệt (thuộc tập hợp này-là tập hợp đứng trc dấu trừ mà không thuộc tập hợp kia) .difference()
+ Set Symetric difference (phép bù): set_1 ^ set_2 (bỏ phần giao nhau) .symmetric_difference()

**6. Các Buil-in functions xử lý Sequence**

3 built-in functions sau đều được dùng kết hợp với lambda 

+ map(): tạo sequences mới dựa trên 1 phương thức và sequence cũ

+ map ==>> function + sequence (có thể 1 hoặc nhiều) = sequence mới

Có thể kết hợp với thư viện operator, truyền vào sub(cộng), mul(nhân) để thực hiện các tính toán cơ bản


+ filter(function,sequence), dùng để lọc các item trong sequence, tạo ra một sequence mới với các item thoả đk của function => luôn luôn trả về True False


+ filter ==>> function + sequence = s_new

+ reduce (function,sequence) -> value: thưởng chỉ tác động lên 2 phần tử. inport functools để sử dụng reduce()

+ reduce = function + sequence = value

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

**1. Làm việc với tập tin văn bản**

+ tổ chức dưới dạng module
+ utf-8: mã để đọc những loại ngôn ngữ có dấu
+ f.read: 1 lần đọc xong hết nội dung file
+ f.close(): dừng việc đang làm và lưu lại file
+ return content: trả về biến content

***Mở file***

fileObject = open(fileName [, accessMode] [, encoding='utf-8'])

f= open('van_ban_2.txt', mode='r', encoding='utf-8')

trong đó, fileName: tên file sẽ truy cập

<img width="1067" alt="Ảnh màn hình 2024-04-07 lúc 13 53 31" src="https://github.com/berylhoang2501/Fundamentals-of-Python/assets/152646327/5312be1e-881d-48ff-9f9d-ed6e7a82fddc">

***Đọc file***

Sử dụng phương thức read ()

- noi_dung = f.read()

- noi_dung = f.readline(): cho phép đọc mỗi lần một dòng có trong file, trong đó ký tự xuống dòng ('\n') sẽ được đọc và ở cuối của chuỗi kết quả.

- noi_dung = f.readlines(): được dùng để đọc tất cả các dòng 1lần và sau đó trả về dưới dạng mỗi dòng là một phần tử trong list. Ký tự xuống
dòng ('\n') sẽ được đọc và ởcuối của từng chuỗi kết quả.

***Ghi file***

Sử dụng phương thức write() hoặc writelines()

- f.writelines(danh_sach_noi_dung)

***Đóng file***

- f. close()

## 24/12/2023: Buổi học 8: Tập tin - Thư mục (cont)

**2. Làm việc với tập tin CSV**

***Đọc file***

- csv.reader(csvfile[, delimiter])

***Ghi file***

Cú pháp:

Tạo file object:

- fileobject =open(csvfile, mode= 'w', newline = ")

Tạo csvwriter object:

- csvWriterObject = csv.writer(fileObject)

Ghi 1dòng dữ liệu vào csvwriter object:

- csvWriter0bject.writerow(list0bject)

**3. Thư viện OS**

## 30/12/2023: Buổi học 9: Module - Package

**1. Module**

**2. Package**

**3. Một số module có sẵn trong Python**

**4. Cài đặt và quản lý package với pip**

PIP là một trình quản lý thư viện cho Python (viết tắt của từ Preferred Installer Program). Đây là một tiện ích dòng lệnh cho phép bạn cài đặt, cài đặt lại hoặc gỡ cài đặt các gói PyPl.

Một số lệnh PIP cơ bản:
- Cài đặt package: pip install ‹package_name>
- Xem chi tiết package đã cài đặt: pip show ‹package_name>
- Liệt kê tất cả các package đã cài đặt: pip list
- Liệt kê tất cả các package đã lỗi thời: pip list --outdated
- Nâng cấp package đã lỗi thời: pip install ‹package_name> --upgrade
- Gỡ bỏ package: pip uninstall ‹package_name>

## 31/12/2023: Buổi học 10: Xử lý ngoại lệ
**1 Giới thiệu**

- Trong Python, các ngoại lệ có thể được xử lý bằng khối lệnh try... except...

**2. Xử lý ngoại lệ trong Python**

- Cú pháp: try... except... else...

<img width="1130" alt="Ảnh màn hình 2024-04-09 lúc 21 34 15" src="https://github.com/berylhoang2501/Fundamentals-of-Python/assets/152646327/784c8ee4-be29-4212-9c9e-aff1ba38d17b">

<img width="1130" alt="Ảnh màn hình 2024-04-09 lúc 21 34 15" src="https://github.com/berylhoang2501/Fundamentals-of-Python/assets/152646327/c031ec63-b944-431d-87ba-72ce22ae29d1"># Fundamentals-of-Python.

- Cú pháp: try.... finally... (Khi ta muốn thực thi khối lệnh trong finally dù cho có lỗi xảy ra trong try hay không.)

<img width="763" alt="Ảnh màn hình 2024-04-09 lúc 21 35 56" src="https://github.com/berylhoang2501/Fundamentals-of-Python/assets/152646327/64be8897-6ee6-49d8-beb2-f0bcd947590b">




