print("In The Name Of GOD")

print("welcome, I am Amir Mahdi")

import math

#نمایش اینکه این برنامه چه کار انجام می دهد.

print("This program solves a quadratic equation: ax² + bx + c = 0")

# Getting coefficients from user
# دریافت ضرایب از کاربر

a = float(input("Enter coefficient a: "))
b = float(input("Enter coefficient b: "))
c = float(input("Enter coefficient c: "))

# Calculating the discriminant
# محاسبه مقدار دلتا (D)

D = b**2 - 4*a*c

# Checking the nature of the roots
# بررسی نوع ریشه‌ها و محاسبه مقدار آن‌ها

#معادله دارای دو ریشه حقیقی است
if D > 0:
    root1 = (-b + math.sqrt(D)) / (2*a)
    root2 = (-b - math.sqrt(D)) / (2*a)
    print(f"The equation has two real roots: {root1:.2f} and {root2:.2f}")
#معادله دارای یک ریشه حقیقی    
elif D == 0:
    root = -b / (2*a)
    print(f"The equation has one real root: {root:.2f}")
#معادله دارای ریشه حقیقی نیست   
else:
    print("The equation has no real roots (complex roots).")