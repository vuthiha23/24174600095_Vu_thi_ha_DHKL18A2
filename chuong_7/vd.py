a =10
if a > 20:
    print("gia tri a tm")
    b=a+1
else:
    print("gia tri a ko tm")
print("ket thuc chuong trinh")

a =10
if a > 20:
    print("gia tri a tm")
    b=a+1
    
print("ket thuc chuong trinh")

a =0
if a > 0:
    print("a la so duong")
elif a<0:
    print("a la so am")
else:
    print("a la so 0")
print("ket thuc chuong trinh") 

for abc in range(10):
    print(abc) 
    
n = int(input("nhap vao so nguyen duong n: "))
for i in range(n):
    if i%2 == 1:
        print(i)             
        
        
        
a = 0
b = 1
n = int(input("nhap vao so nguyen duong n: "))
for i in range(n):
    print(a)
    sum_a_b = a + b
    a = b 
    b = sum_a_b
    
for i in range(10):
    if i == 4:
        break
    print(i)
else:
    print("chay cau lenh else")    
        
for i in range(10):
    if i == 4:
        continue
    print(i) 
    
  # break (dừng) continue (bỏ qua)   
  
  
  
  
  
# print("Hello world")

a = "Hello world"
b = 'Hello world'

c = 'Bạn A nói: "Abcd"'
d = "Bạn A nói: 'Abcd'"

#Kiểu dữ liệu tuần tự là kiểu dữ liệu có thể truy cập vào các phần tử ở trong nó
#Truy cập sử dụng index (danh mục)

print(a[4])

#[start:stop:step]
#start: vị trí bắt đầu
#stop: vị trí kết thúc
#step: khoảng cách giữa các bước
print(a[1:7]) #lấy các giá trị từ start đến stop-1
print(a[:7])
print(a[1:])
print(a[:])
#mặc định của step = 1
print(a[1:7:2])
print(a[1:7:])
print(a[:7:2])
print(a[1::2])
print(a[::2])
print(a[::])
print(a[::-1])

print(range(5)) #0,1,2,3,4
#range cũng sử dụng start, stop, step
range(1,5)
range(1,5,2)


for item in a:
    print(item)
    
# #Hàm đo độ dài kiểu dữ liệu tuần tự: len
print(len(a))
range(len(a)) #thu được chỉ mục chạy từ 0 đến len(a)-1 = 10

for i in range(len(a)):
    print(a[i])
    
#tính chất của kiểu dữ liệu chuỗi ký tự:
# - Có thể truy cập
# - Không thể chỉnh sửa
# - Không thể sắp xếp

b = "Hello" + "world"
print(b)

n = int(input("nhap vao so nguyen duong: "))
if n > 0:
    print("Da nhap dung so nguyen duong")
    
c = ""    
for i in range(len(a)):
    if a[i] == "a":
        c = c + i

for i in a:
    print(i)


#Các phương thức trong xử lý chuỗi ký tự
a = "Hello world"
#Các phương thức kiểm tra (trả về cho mình True hoặc False)
#các phương thức này sẽ thường bắt đầu bằng chữ "is"

# - kiểm tra chuỗi có phải alphanumeric (chỉ có ký tự số và chữ hay không)
print(a.isalnum())
# - kiểm tra chuỗi có toàn số hay không (numeric)
print(a.isnumeric())
# - kiểm tra chuỗi có toàn chữ hay không (character)
print(a.isalpha())
# - Kiểm tra chuỗi có nằm trong bảng mã ascii hay không
print(a.isascii())
# - Kiểm tra chuỗi có phải kiểu số hay không
print(a.isdigit()) #Số thông thường
print(a.isdecimal()) # số thập phân
#- kiểm tra xem chuỗi có khoảng trống hay không
print(a.isspace())
#- kiểm tra in hoa in thường
print(a.isupper())
print(a.islower())

#- kiểm tra ký tự tồn tại trong chuỗi
print(a.find("llo"))
print(a.count("l"))
print(a.index("s"))


#Phương thức biến đổi (các phương thức này trả về chuỗi ký tự mới, không thay đổi chuỗi ký tự ban đầu)
a = "Hello world"
#- Xóa ký tự đầu và cuối của chuỗi
a_sua = a.strip()
a_sua = a.lstrip()
a_sua = a.rstrip()

#- Thay thế ký tự bất kỳ
a_sua = a.replace("l","w")

# - biến đổi viết hoa viết thường
a_sua = a.upper()
a_sua = a.lower()
a_sua = a.capitalize()        