
from operations import add, subtract, multiply, divide


def get_number(prompt):
    while True:
        try:
            return float(input(prompt))
        except ValueError:
            print("Please enter a valid number.")


def main():
    print("=== Simple Calculator ===")

    while True:
        print("\n1. Add")
        print("2. Subtract")
        print("3. Multiply")
        print("4. Divide")
        print("5. Exit")

        choice = input("Choose operation (1-5): ").strip()

        if choice == "5":
            print("Goodbye!")
            break

        if choice not in ("1", "2", "3", "4"):
            print("Invalid choice, try again.")
            continue

        a = get_number("First number: ")
        b = get_number("Second number: ")

        try:
            if choice == "1":
                result = add(a, b)
            elif choice == "2":
                result = subtract(a, b)
            elif choice == "3":
                result = multiply(a, b)
            else:
                result = divide(a, b)

            print("Result:", result)

        except ZeroDivisionError:
            print("Error: Cannot divide by zero.")


if __name__ == "__main__":
    main()
