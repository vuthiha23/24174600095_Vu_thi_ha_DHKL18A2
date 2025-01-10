n = int(input("nhap so nguyen duong :"))
if n > 0:
    x = 0
    for i in range(1,n+1):
        x=x+i
    s = x / (n +1) 
    print(f"ket qua la :{s}")
else:
    print("yeu cau nhap so duong")       
        
        