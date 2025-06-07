import random

with open("data.txt", "w") as f:
    for _ in range(1000):
        f.write(f"{random.random()}\n")

print("File Sakhte shode")

numbers = []
with open("data.txt", "r") as f:
    for line in f:
        try:
            num = float(line.strip())
            numbers.append(num)
        except ValueError:
            print(f"kate {line.strip()} nadide grafte shod.")
if numbers:
    average = sum(numbers) / len(numbers)
    print(f"Average of {len(numbers)} numbers: {average}")
else:
    print("Adady vjod ndasht")
