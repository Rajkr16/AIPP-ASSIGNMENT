def count_vowels(input_string):
    vowels = "aeiouAEIOU"
    count = sum(1 for char in input_string if char in vowels)
    return count

if __name__ == "__main__":
    user_input = input("Enter a string: ")
    print("number of vowel-",count_vowels(user_input))