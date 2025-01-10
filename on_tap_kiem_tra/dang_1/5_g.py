n = int(input("nhap so nguyen duong:"))
if n < 8:
    print("yeu cau nhap so nguyen duong lon hon 8")
else:
    P = 0
    for i in range(8,n+1):
        tu_so = 1
        for i in range(1,n + 1):
            tu_so= tu_so*i
        mau_so = 1
        for j in range(4,i +1):
            mau_so*=(1/j) 
        
        P=P+(tu_so/mau_so)
        break
    print(f"gia tri P la {P}")      
        