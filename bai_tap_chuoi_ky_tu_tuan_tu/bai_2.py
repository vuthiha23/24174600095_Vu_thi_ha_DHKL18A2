ds_so = []

while True:
    n = input("Nhap vao so pan tu n trong danh sach: ")
    if n.isdigit() == False:
      print("Yeu cau nhap lai so nguyen duong!!")
    else:
        n = int(n)
        break

for i in range(n):
    while True:
        so = input(f"Nhap gia tri so thu {i + 1}: ")
        if so.isdigit() == False:
          print("Yeu cau nhap vao so!!")
        else:
          so = float(so)      
          break
          ds_so.append
        
tong = sum(ds_so)
print(f"Tong cac so vua nhap: {tong}")


ds_so = []
while True:
   n = input("Nhap vao so phan tu n trong danh sach: ")
   if n.isdigit() == False:
      print("Yeu cau nhap lai so nguyen duong!!")
        
   else:
       n = int(n)
       break
   
   
for i in range(n):
    while True:
      so = input(f"Nhap gia tri so thu {i + 1}: ")
      if so.count('-') == 1 and so.replace('-','').isdigit():
          so = float(so)
          break
else:
    print("Yeu cau nhap vao so!!")
            
ds_so.append(so)

tong = sum(ds_so)
print(f"Tong cac so vua nhap: {tong}")
