def format_name():
    # Get full name from user
    full_name = input("Enter full name: ").strip()
    
    # Split the name into parts
    name_parts = full_name.split()
    
    # Check if the input contains at least first and last name
    if len(name_parts) >= 2:
        # Get the last name (last part) and first name (first part)
        last_name = name_parts[-1]
        first_name = name_parts[0]
        
        # Format as "Last, First"
        formatted_name = f"{last_name}, {first_name}"
        return formatted_name
    else:
        return "Please enter both first and last name"

# Test the function
if __name__ == "__main__":
    formatted = format_name()
    print(formatted)