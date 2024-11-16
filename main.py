def fibonacci(n):
    if n <= 0:
        return "Input must be a positive integer"
    elif n == 1:
        return 0
    elif n == 2:
        return 1

    a, b = 0, 1

    for _ in range(2, n):
        a, b = b, a + b
    return b


num = int(input("Enter the position of the fibonacci sequence: "))
print(f"The {num}th Fibonacci number is: {fibonacci(num)}")
