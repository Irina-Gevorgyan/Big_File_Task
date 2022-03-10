import random

file_rows_count = int(input("Enter the number of digits in file: "))

while file_rows_count < 0:
    file_rows_count = int(input("Enter the positive number: "))

digits_file = open('ages', 'w+')

for i in range(file_rows_count):
    age = random.randint(0, 120)

    digits_file.write(f"{str(age)} \n")

digits_file.close()