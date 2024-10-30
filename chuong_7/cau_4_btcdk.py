a = input("nhap gia tri a")
b = input("nhap gia tri b")
c = input("nhap gia tri c")
a = int(a)
b = int(b)
c = int(c)
if a<0 and b<0 and c<0:
    if a!=0:
        delta = b**2 - 4*a*c
        if delta > 0:
            x_1 = (-b + delta**(1/2)/(2*a))
            x_2 = (-b - delta**(1/2)/(2*a))
            print("phuong trinh co hai nghiem phan biet ")