def greet_user(name, gender):
    gender_lower = gender.lower()
    
    if gender_lower == "male":
        title = "Mr."
    elif gender_lower in ["female", "woman"]:
        title = "Mrs."
    elif gender_lower in ["non-binary", "nonbinary", "neutral", "other", "agender", "genderqueer"]:
        title = "Mx."
    else:
        # Default to gender-neutral title for unrecognized values
        title = "Mx."
    
    return f"Hello, {title} {name}! Welcome."

name = input("Enter your name: ")
gender = input("Enter your gender: ")
print(greet_user(name, gender))