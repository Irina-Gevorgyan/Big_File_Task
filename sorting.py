import sys

digits_file = open('ages', 'r')

ages = [0] * 121

for line in digits_file:
    ages[int(line.strip())] += 1

digits_file = open('ages', 'w')

for i in range(0,121):
    print(f"Count of {i} years old people are {ages[i]}")
    for counter in range(0,ages[i]):
        digits_file.write(f"{str(i)}\n")

digits_file.close()