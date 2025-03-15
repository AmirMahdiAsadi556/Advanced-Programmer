while True:
    # دریافت عدد معتبر از کاربر
    while True:
        try:
            n = int(input("Enter a positive number: "))
            if n > 0:
                break  # اگر عدد معتبر بود، از حلقه خارج شو
            else:
                print("Please enter a number greater than zero!")
        except ValueError:
            print("Invalid input! Please enter a valid number.")

    i = 0
    while i <= n:
        print(f"2^{i} = {2 ** i}")
        i += 1

    # پرسش برای اجرای مجدد
    again = input("Do you want to try again? (y/n): ").strip().lower()
    if again != 'y':
        print("Goodbye! 👋")
        break