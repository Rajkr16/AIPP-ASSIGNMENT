def bubble_sort(arr):
    """
    Sorts an array using bubble sort algorithm.
    """
    n = len(arr)
    for i in range(n):
        swapped = False
        for j in range(0, n - i - 1):
            if arr[j] > arr[j + 1]:
                arr[j], arr[j + 1] = arr[j + 1], arr[j]
                swapped = True
        if not swapped:
            break
    return arr


def is_sorted(arr):
    """
    Checks if an array is sorted in ascending order.
    """
    for i in range(len(arr) - 1):
        if arr[i] > arr[i + 1]:
            return False
    return True


# Test the implementation
if __name__ == "__main__":
    test_array = [64, 34, 25, 12, 22, 11, 90]
    print("Original array:", test_array)
    
    sorted_array = bubble_sort(test_array.copy())
    print("Sorted array:", sorted_array)
    
    print("Is sorted?", is_sorted(sorted_array))