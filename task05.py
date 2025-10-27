def find_largest_number():
    # Taking user input
    numbers = input("Enter numbers separated by spaces: ")
    
    # Converting input string to a list of integers
    number_list = list(map(int, numbers.split()))
    
    # Finding the largest number
    largest_number = max(number_list) if number_list else None
    
    return largest_number

if __name__ == "__main__":
    largest = find_largest_number()
    if largest is not None:
        print(f"The largest number is: {largest}")
    else:
        print("No numbers were entered.")