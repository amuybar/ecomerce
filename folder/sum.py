numbers = input("Enter a list of integers separated by spaces: ").split()
numbers = [int(num) for num in numbers]
sum_of_numbers = sum(numbers)
print("Sum of the numbers:", sum_of_numbers)
