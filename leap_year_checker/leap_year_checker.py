print("In The Name Of GOD")

print("welcome, I am Amir Mahdi")

while True:
    
    year = input("Please enter a year or type 'exit': ")

    if year.lower() == "exit":
        print("Goodbye!")
        break  # Exit the loop

    try:
        year = int(year)

        if (year % 4 == 0 and year % 100 != 0) or (year % 400 == 0):
            print(f"Yes! The year {year} is a leap year. :) ")
        else:
            print(f"No, the year {year} is not a leap year. :( ")

    except ValueError:
        print("Invalid input! Please enter a valid year or type 'exit'.")
