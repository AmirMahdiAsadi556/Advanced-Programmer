SUM = 0.0
count = 0

with open("data.txt", "r") as f:
    for line in f:
        try:
            num = float(line.strip())
            SUM += num
            count += 1
        except ValueError:
            print(f" kate {line.strip()} baresi nashod")

if count > 0:
    average = SUM / count
    print(f"Average of {count} numbers: {average}")
else:
    print("Adad motabar vjod ndard")
