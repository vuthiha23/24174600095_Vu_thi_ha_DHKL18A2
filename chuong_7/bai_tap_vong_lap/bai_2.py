n = int(input("nhap so nguyen duong n:"))
S1 = 0 
for i in range(1,n +1):
    S1 += i
print(f"S1 = {S1}")
S2 = 1 
for i in range(1,n):
    S2 *= i
print(f"S2 = {S2}")
S3 = 0
for i in range(1,n + 1):
    S3 += ((-1) ** (i + 1))/ i
print(f"S3 = {S3}")
S4 = 0
for k in range(0,n + 1):
    S4 += k / (k+2)
print(f"S4 = {S4}")