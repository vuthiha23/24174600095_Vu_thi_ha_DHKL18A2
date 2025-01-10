n = int(input("nhap so nguyen duong :"))
if n > 4:
    a = 0
    for i in range(4,n+1):# vòng lặp từ 4 đến n
        a=a+((i+1)/(i-1))
    b = 0     
    for i in range(1,n+1):
        b=b+(i/i+1) 
    s = a + b  
    print(f"s = {s}")    
else:
    print("yeu cau nhap so nguyen duong")  
          
        