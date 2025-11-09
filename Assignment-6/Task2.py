def print_multiples_for_loop(number):
    """
    Print the first 10 multiples of a number using a for loop.
    
    Args:
        number (int): The number to find multiples of
    """
    print(f"First 10 multiples of {number} (using for loop):")
    for i in range(1, 11):
        multiple = number * i
        print(f"{number} x {i} = {multiple}")


def print_multiples_while_loop(number):
    """
    Print the first 10 multiples of a number using a while loop.
    
    Args:
        number (int): The number to find multiples of
    """
    print(f"\nFirst 10 multiples of {number} (using while loop):")
    i = 1
    while i <= 10:
        multiple = number * i
        print(f"{number} x {i} = {multiple}")
        i += 1


def print_multiples_list_comprehension(number):
    """
    Print the first 10 multiples of a number using list comprehension.
    
    Args:
        number (int): The number to find multiples of
    """
    print(f"\nFirst 10 multiples of {number} (using list comprehension):")
    multiples = [number * i for i in range(1, 11)]
    for i, multiple in enumerate(multiples, 1):
        print(f"{number} x {i} = {multiple}")


# Main execution
if __name__ == "__main__":
    # Get number from user input
    num = int(input("Enter a number: "))
    
    # Demonstrate different looping approaches
    print_multiples_for_loop(num)
    print_multiples_while_loop(num)
    print_multiples_list_comprehension(num)

