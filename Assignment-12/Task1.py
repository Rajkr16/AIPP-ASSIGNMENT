def linear_search(lst, target):
    """
    Search for a target value in a list and return its index.
    
    Args:
        lst: The list to search in
        target: The value to search for
    
    Returns:
        The index of the target if found, -1 otherwise
    """
    for i in range(len(lst)):
        if lst[i] == target:
            return i
    return -1


# Example usage
if __name__ == "__main__":
    my_list = [10, 23, 45, 70, 11, 15]
    search_value = 70
    
    result = linear_search(my_list, search_value)
    
    if result != -1:
        print(f"Element {search_value} found at index {result}")
    else:
        print(f"Element {search_value} not found in the list")