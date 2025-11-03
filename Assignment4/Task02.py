def cm_to_inches():
    try:
        # Get user input in centimeters
        cm = float(input("Enter length in centimeters: "))
        
        # Convert centimeters to inches (1 inch = 2.54 cm)
        inches = cm / 2.54
        
        # Display the result rounded to 2 decimal places
        print(f"{cm} centimeters is equal to {round(inches, 2)} inches")
    except ValueError:
        print("Please enter a valid number")

# Call the function
cm_to_inches()