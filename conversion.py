def main():
    # Prompt the user for input
    try:
        # taking kilometers input from the user
        kilometers = float(input("Enter value in kilometers: "))

        # conversion factor
        conv_fac = 0.621371
        
        # calculate miles
        miles = kilometers * conv_fac

        # print result
        print('%0.2f kilometers is equal to %0.2f miles' %(kilometers,miles))
    
    except ValueError:
        print("Invalid input! Please enter numeric values.")

if __name__ == "__main__":
    main()