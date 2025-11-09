def count_down(n):
    while n >= 0:
        print(n)
        n -= 1  # Decrement n to count down (was n += 1 which caused infinite loop)

