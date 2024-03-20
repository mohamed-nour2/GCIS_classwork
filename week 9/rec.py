def sum_numbers_in_file():
    total_sum = 0
    with open("numbers.txt", "r") as file:
        for line in file:
            number = int(line.strip())
            total_sum += number
    print("Sum of numbers:", total_sum)


sum_numbers_in_file()
