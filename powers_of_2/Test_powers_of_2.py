print("In The Name Of GOD")

print("welcome, I am Amir Mahdi")

print("This program prints powers of 2.")
# تعداد توان‌ها را از کاربر می‌گیریم
n = int(input("Enter the number of terms you want: "))  
# شمارنده از 0 شروع می‌شود
i = 0  
while i <= n:
    # توان ۲ را محاسبه و چاپ می‌کنیم
    print(f"2^{i} = {2**i}")  
    # مقدار شمارنده را افزایش می‌دهیم
    i += 1  
    #مشکل دارد :اگر کاربر مقدار را به‌صورت عدد منفی یا حرف وارد کند، برنامه کرش می‌کند
