n = 10        
while n > 2: #true
    printn(f"chay vong lap {n}")
    n = n - 1
    
    
    
    
    
    
    
n = 10        
while n > 2: #true
    print(f"chay vong lap {n}")
    n = n - 1    
    if n == 6:
        break 
    
    
    
    
    
n = 10        
while n > 2: #true
    print(f"chay vong lap {n}")
    n = n - 1
    if n == 6:
        continue     
    
    
    
n = 10        
while n > 2: #true
    n = n - 1
    if n == 6:
        continue    
    print(f"chay vong lap {n}")
    
n = 20
while True:
    for i in range(1,n):
        if n%i==0 and i!=1 and i!=n:
            n = n - 1
            break
    else:
        break
    if n < 1:
        break
print(f"so nguyen to la {n}")    

k = 10
tong_l = 0
for l in range(1,k):
    tong_l = tong_l + (l + 1)
            
            
n = int(input("nhap gia tri nguyen duong n :"))
tong_n = 0
for k in range(1,n +1):
    tong_l = 0
    for l in range(1,k):
        tong_l = tong_l + (l + 1)
    tong_n = tong_n + (tong_l/k) 
    
print(f"ket qua:{tong_n}")       


k = 10 
tong_l = 0
for l in range(1, k+1):
    tong_l = tong_l + (l + 1)
    
giai_thua_k = 1
for i in range(1,k+1):
    giai_thua_k = giai_thua_k*i
    
n = int(input("nhap so nguyen duong n:")) 
tong_n = 0
for k in range(1,n+1):
    tong_l = 0
    for l in range(1, k+1):
        tong_l = tong_l + (l + 1)
    
    giai_thua_k = 1
    for i in range(1,k+1):
        giai_thua_k = giai_thua_k*i
    
    tong_n = tong_l/giai_thua_k
print(f"ket qua:{tong_n}")    
                                    