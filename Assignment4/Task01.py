def check_leap_year():
    try:
        # Get year input from user
        year = int(input("Enter a year to check if it's a leap year: "))
        
        # Check leap year conditions
        if (year % 4 == 0 and year % 100 != 0) or (year % 400 == 0):
            print(f"{year} is a leap year!")
        else:
            print(f"{year} is not a leap year.")
            
    except ValueError:
        print("Please enter a valid year (integer number)")

# Call the function
if __name__ == "__main__":
    check_leap_year()