numbers = [1, 2, 3]

# This will cause an IndexError - accessing index 5 when list only has indices 0, 1, 2
# print(numbers[5])  # Uncomment to see the error

# Resolving the IndexError using try-except
try:
    print(numbers[5])
except IndexError:
    print("IndexError: List index out of range. The list only has", len(numbers), "elements (indices 0 to", len(numbers)-1, ")")

# Alternative solution: Check the index before accessing
index = 5
if index < len(numbers):
    print(f"Value at index {index}: {numbers[index]}")
else:
    print(f"IndexError prevented: Index {index} is out of range. List has {len(numbers)} elements (indices 0 to {len(numbers)-1})")

