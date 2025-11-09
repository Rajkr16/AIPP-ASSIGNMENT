# Age Classification using Ternary and Match-Case

def classify_age_ternary(age):
    return ("Invalid age" if age < 0 else
            "Infant" if age <= 2 else
            "Toddler" if age <= 5 else
            "Child" if age <= 12 else
            "Early Teen" if age <= 15 else
            "Late Teen" if age <= 19 else
            "Young Adult" if age <= 29 else
            "Adult" if age <= 39 else
            "Middle-aged" if age <= 49 else
            "Mature Adult" if age <= 64 else
            "Senior" if age <= 74 else
            "Elderly" if age <= 89 else
            "Very Elderly")

def classify_age_match_case(age):
    if age < 0: return "Invalid age"
    match age:
        case n if n <= 2: return "Infant"
        case n if n <= 5: return "Toddler"
        case n if n <= 12: return "Child"
        case n if n <= 15: return "Early Teen"
        case n if n <= 19: return "Late Teen"
        case n if n <= 29: return "Young Adult"
        case n if n <= 39: return "Adult"
        case n if n <= 49: return "Middle-aged"
        case n if n <= 64: return "Mature Adult"
        case n if n <= 74: return "Senior"
        case n if n <= 89: return "Elderly"
        case _: return "Very Elderly"

# Main Program
age = int(input("Enter your age: "))
print("\nTernary Method:", classify_age_ternary(age))
print("Match-Case Method:", classify_age_match_case(age))
