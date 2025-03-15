print("In The Name Of GOD")

print("welcome, I am Amir Mahdi")

import math

while True:
 
 a = float(input("Enter coefficient a: "))
 b = float(input("Enter coefficient b: "))
 c = float(input("Enter coefficient c: "))   

 D = b**2 - 4*a*c

 if D > 0:
        root1 = (-b + math.sqrt(D)) / (2*a)
        root2 = (-b - math.sqrt(D)) / (2*a)
        print(f"The equation has two real roots: {root1:.2f} و {root2:.2f}")
 elif D == 0:
        root = -b / (2*a)
        print(f"یک ریشه حقیقی (مضاعف): {root:.2f}")
 else:
        print("The equation has no real roots (complex roots).")

 again = input("Try again (y/n): ")
 if again.lower() != 'y':
        break
