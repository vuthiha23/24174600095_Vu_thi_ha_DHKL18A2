import math
# nhập giá trị của x trên máy tính 
x = float(input("nhập giá trị của x :  "))
log_4_x = math.log(x) / math.log(4)
log_2_x = math.log(x) / math.log(2)
f_x = log_4_x + log_2_x
print(f"giá trị của biểu thức f(x) là : {round(f_x,2)}")