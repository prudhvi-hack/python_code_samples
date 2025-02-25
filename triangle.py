def main():
    try:
        a = float(input('Enter first side: '))
        b = float(input('Enter second side: '))
        c = float(input('Enter third side: '))
        
        # calculate the semi-perimeter
        s = (a + b + c) / 2

        # calculate the area
        area = (s*(s-a)*(s-b)*(s-c)) ** 0.5
        print('The area of the triangle is %0.2f' %area)
        
    except ValueError:
        print("Invalid input! Please enter numeric values.")

if __name__ == "__main__":
    main()