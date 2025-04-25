print("In The Name Of GOD")

print("welcome, I am Amir Mahdi")

salary = int(input("Enter your monthly salary :"))

#اگه حقوق کمتر از ۵ میلیون باشه، مالیات ۵٪ حساب می‌شه#
if salary < 5000000:
    tax = salary * 0.05
#بین ۵ تا ۱۰ میلیون، مالیات ۱۰٪ حساب می‌شه #  
elif salary >= 5000000 and salary <= 10000000:
    tax = salary * 0.10
#بیشتر از ۱۰ میلیون، مالیات ۲۰٪ حساب می‌شه
else:
    tax = salary * 0.20

# چاپ مالیات
print("The amount of your tax is equal to:", int(tax), "toman")