# average.py
numbers = input("Enter numbers separated by spaces: ").split()
numbers = [float(num) for num in numbers]  # Convert to float
average = sum(numbers) / len(numbers)
print(f"The average is: {average}")

