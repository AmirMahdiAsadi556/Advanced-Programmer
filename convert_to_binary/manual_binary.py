number = int(input("Enter an integer number: "))

if number == 0:
    print("Binary: 0")
else:
    binary = ""  # در ابتدا هیچ بیتی نداریم، بنابراین رشته باید خالی شروع شود
    while number > 0:
        remainder = number % 2        # باقیمانده
        binary = str(remainder) + binary  # اضافه کردن به اول رشته
        number = number // 2          # تقسیم عدد بر 2 (عدد صحیح باید باشد)
    print("Binary:", binary)
