x = float(input("x = "))
y = float(input("y = "))
a = float(input("a = "))
b = float(input("b = "))
ban_kinh_R = float(input("nhap ban kinh R : "))
do_dai_IM = ((a-x)**2+(b-y)**2)**(1/2)
if do_dai_IM <= ban_kinh_R:
    print("True")
else:
    print("False")    
