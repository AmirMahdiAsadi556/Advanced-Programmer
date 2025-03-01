print("In The Name Of GOD")

print("welcome, I am Amir Mahdi")

year = int(input("Please enter a year: "))

if (year % 4 == 0 and year % 100 != 0) or (year % 400 == 0):
    print(f"Yes, The year {year} is a leap year. :) ")
else:
    print(f"No, the year {year} is not a leap year. :( ") 
