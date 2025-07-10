import random

def generate_random_numbers(n, a, b):
    numbers = [random.randint(a, b) for _ in range(n)]
    odd_count = sum(1 for num in numbers if num % 2 != 0)
    even_count = n - odd_count
    return numbers, odd_count, even_count

n = int(input("Enter how many random numbers you want to generate (N): "))
a = int(input("Enter the lower bound of the range (A): "))
b = int(input("Enter the upper bound of the range (B): "))

numbers, odd, even = generate_random_numbers(n, a, b)

print("\nGenerated Numbers:", numbers)
print("Odd values =", odd)
print("Even values =", even)