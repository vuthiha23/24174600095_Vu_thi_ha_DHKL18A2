def kiem_tra_chuoi_so(s):
    """
    Kiểm tra xem một chuỗi có phải là chuỗi số nguyên hay không.

    Args:
        s (str): Chuỗi cần kiểm tra.

    Returns:
        bool: True nếu chuỗi là chuỗi số nguyên, False nếu không.
    """
    if not s:  # Kiểm tra chuỗi rỗng
        return False
    
    # Loại bỏ dấu cách đầu cuối chuỗi
    s = s.strip()

    # Kiểm tra xem chuỗi có dấu '-' hoặc '+' ở đầu và các ký tự còn lại là số
    if s[0] in ('-', '+'):
        return s[1:].isdigit()

    # Kiểm tra nếu toàn bộ chuỗi là số
    return s.isnumeric()
print(kiem_tra_chuoi_so("123"))
print(kiem_tra_chuoi_so("+123"))
print(kiem_tra_chuoi_so("-123"))
print(kiem_tra_chuoi_so("12.3"))
print(kiem_tra_chuoi_so("abc"))


