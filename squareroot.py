def main():
    try:
        num = float(input('Enter a number: '))        
        
        # calculate the sqaure root
        num_sqrt = num ** 0.5
        print('The square root of %0.3f is %0.3f'%(num ,num_sqrt))

    except ValueError:
        print("Invalid input! Please enter numeric values.")

if __name__ == "__main__":
    main()