i = int(input("Nhập chỉ số cột i (0 đến n-1): "))
j = int(input("Nhập chỉ số cột j (0 đến n-1): "))
m = int(input("Nhập số hàng m: "))
n = int(input("Nhập số cột n: "))
A = []
print(f"Nhập vào ma trận kích thước {m}x{n}:")
for i in range(m):
    hang = list(map(int, input(f"Nhập hàng {i + 1}: ").split()))
    while len(hang) != n:
        print(f"Vui lòng nhập đúng {n} phần tử.")
        hang = list(map(int, input(f"Nhập hàng {i + 1}: ").split()))
    A.append(hang)

print("ma tran A la :")
for hang in A:
    print(" ".join(map(str, hang)))   
if i < 0 or i >= n or j < 0 or j >= n:
     print("Chỉ số cột không hợp lệ!")
else:
    print("Ma trận sau khi đổi chỗ:")
    for hang[i],hang[j] = hang[j],hang[i] in A:
print(" ".join(map(str, hang))) 