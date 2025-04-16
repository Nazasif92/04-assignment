def sum_of_numbers(numbers):
    total = 0
    for num in numbers:
        total += num
    return total

# Example list
my_list = [3, 27, 15]

# Function call
result = sum_of_numbers(my_list)

# Print the result
print(f"The sum of the numbers is: {result}")