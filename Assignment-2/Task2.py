def is_palindrome(text):
    # Remove spaces and convert to lowercase
    text = text.replace(" ", "").lower()
    # Compare the string with its reverse
    return text == text[::-1]

# Get input from user
user_input = input("Enter a word or phrase to check if it's a palindrome: ")

# Check if it's a palindrome and print result
if is_palindrome(user_input):
    print(f"'{user_input}' is a palindrome!")
else:
    print(f"'{user_input}' is not a palindrome.")