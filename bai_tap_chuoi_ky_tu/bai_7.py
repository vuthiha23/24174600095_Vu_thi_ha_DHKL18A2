nhap_vao_chuoi = input("nhap vao ky tu:")
if nhap_vao_chuoi.isdecimal() and  nhap_vao_chuoi.isdigit():    #isdecimal kiểm tra xem số thập phân hay không isdigit kiểm tra phải là só hay k
    print("chuoi nay la so thap phan") 
else:
    print(" chuoi nay khong phai la so thap phan")