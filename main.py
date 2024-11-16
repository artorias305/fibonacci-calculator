import matplotlib.pyplot as plt

# Memoization to store previously calculated Fibonacci numbers
memo = {}


def fibonacci(n):
    if n in memo:
        return memo[n]
    if n <= 0:
        return "Input must be a positive integer."
    elif n == 1:
        memo[n] = 0
    elif n == 2:
        memo[n] = 1
    else:
        memo[n] = fibonacci(n - 1) + fibonacci(n - 2)
    return memo[n]


def fibonacci_sequence_up_to_n(n):
    sequence = []
    for i in range(1, n + 1):
        sequence.append(fibonacci(i))
    return sequence


def display_menu():
    print("\nFibonacci Calculator")
    print("1. Find the nth Fibonacci number")
    print("2. Generate Fibonacci sequence up to nth number")
    print("3. Visualize Fibonacci sequence (Line and Bar Charts)")
    print("4. Exit")


def visualize_sequence(sequence):
    positions = list(range(1, len(sequence) + 1))

    # Create a figure with two subplots
    fig, axes = plt.subplots(1, 2, figsize=(14, 6))

    # Line chart
    axes[0].plot(positions, sequence, marker="o", color="b")
    axes[0].set_title("Fibonacci Sequence (Line Chart)")
    axes[0].set_xlabel("Position (n)")
    axes[0].set_ylabel("Fibonacci Number")
    axes[0].grid(True)

    # Bar chart
    axes[1].bar(positions, sequence, color="orange", edgecolor="black")
    axes[1].set_title("Fibonacci Sequence (Bar Chart)")
    axes[1].set_xlabel("Position (n)")
    axes[1].set_ylabel("Fibonacci Number")
    axes[1].grid(axis="y")

    # Adjust layout and show the plot
    plt.tight_layout()
    plt.show()


def main():
    while True:
        display_menu()
        choice = input("Enter your choice (1-4): ")

        if choice == "1":
            try:
                n = int(input("Enter the position (n): "))
                if n <= 0:
                    print("Please enter a positive integer.")
                else:
                    print(f"The {n}th Fibonacci number is: {fibonacci(n)}")
            except ValueError:
                print("Invalid input. Please enter a positive integer.")

        elif choice == "2":
            try:
                n = int(input("Enter the number of terms: "))
                if n <= 0:
                    print("Please enter a positive integer.")
                else:
                    sequence = fibonacci_sequence_up_to_n(n)
                    print(f"Fibonacci sequence up to {n} terms: {sequence}")
            except ValueError:
                print("Invalid input. Please enter a positive integer.")

        elif choice == "3":
            try:
                n = int(input("Enter the number of terms to visualize: "))
                if n <= 0:
                    print("Please enter a positive integer.")
                else:
                    sequence = fibonacci_sequence_up_to_n(n)
                    visualize_sequence(sequence)
            except ValueError:
                print("Invalid input. Please enter a positive integer.")

        elif choice == "4":
            break

        else:
            print("Invalid choice. Please select an option between 1 and 4.")


if __name__ == "__main__":
    main()
