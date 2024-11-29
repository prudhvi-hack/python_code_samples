def main():
    # Prompt the user for input
    try:
        x = input('Enter value of x: ')
        y = input('Enter value of y: ')
        
        # create a temporary variable and swap the values
        temp = x
        x = y
        y = temp
        
        # Print the result
        print('The value of x after swapping: {}'.format(x))
        print('The value of y after swapping: {}'.format(y))

    except ValueError:
        print("Invalid input! Please enter numeric values.")

if __name__ == "__main__":
    main()