import math
def so_chinh_phuong(n):
    """
    Kiểm tra số có phải số chính phương hay không.

    Args:
        n (int): Số cần kiểm tra.

    Returns:
        bool: True nếu số là chính phương, False ngược lại.
    """
    if n < 0:
        return False
    so = math.sqrt(n)
    return so == int(so)
print(so_chinh_phuong(9))