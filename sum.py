def main():
    # Prompt the user for input
    try:
        num1 = float(input("Enter the first number: "))  # Take first number as input
        num2 = float(input("Enter the second number: "))  # Take second number as input

        # Calculate the sum
        result = num1 + num2
        
        # Print the result
        print(f"The sum of {num1} and {num2} is: {result}")

    except ValueError:
        print("Invalid input! Please enter numeric values.")

if __name__ == "__main__":
    main()