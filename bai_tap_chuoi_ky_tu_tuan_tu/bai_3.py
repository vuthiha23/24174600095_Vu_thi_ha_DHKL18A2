n = int(input("Nhập vào số nguyên dương n: "))
A = []  
B = []  
for i in range(n):
    if i % 2 == 0:
        B.append(i)  
    else:
        A.append(i)  
A.sort(reverse=True)
B.sort(reverse=True)
print("Danh sách A (các số lẻ nhỏ hơn n):", A)
print("Danh sách B (các số chẵn nhỏ hơn n):", B)