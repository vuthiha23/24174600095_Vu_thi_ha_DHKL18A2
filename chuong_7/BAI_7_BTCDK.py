# Nhập các hệ số từ bàn phím
a1 = float(input("Nhập hệ số a1: "))
b1 = float(input("Nhập hệ số b1: "))
c1 = float(input("Nhập hệ số c1: "))
a2 = float(input("Nhập hệ số a2: "))
b2 = float(input("Nhập hệ số b2: "))
c2 = float(input("Nhập hệ số c2: "))
D = a1 * b2 - a2 * b1
Dx = c1 * b2 - c2 * b1
Dy = a1 * c2 - a2 * c1
if D != 0:
    # Hệ có nghiệm duy nhất
    x = Dx / D
    y = Dy / D
    print(f"Hệ có nghiệm duy nhất: x = {x}, y = {y}")
else:
    # Xét trường hợp đặc biệt khi D = 0
    if Dx == 0 and Dy == 0:
        print("Hệ có vô số nghiệm.")
    else:
        print("Hệ vô nghiệm.")
