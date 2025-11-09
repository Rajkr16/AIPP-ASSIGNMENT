def classify_age_group(age):
    """
    Classify age groups using nested if-elif-else conditionals.
    
    Args:
        age (int): The age to classify
    
    Returns:
        str: The age group classification
    """
    if age < 0:
        return "Invalid age"
    elif age <= 12:
        # Child category with nested conditions
        if age <= 2:
            return "Infant (0-2 years)"
        elif age <= 5:
            return "Toddler (3-5 years)"
        elif age <= 8:
            return "Child (6-8 years)"
        else:
            return "Pre-teen (9-12 years)"
    elif age <= 19:
        # Teenager category with nested conditions
        if age <= 15:
            return "Early Teen (13-15 years)"
        else:
            return "Late Teen (16-19 years)"
    elif age <= 64:
        # Adult category with nested conditions
        if age <= 39:
            if age <= 29:
                return "Young Adult (20-29 years)"
            else:
                return "Adult (30-39 years)"
        elif age <= 49:
            return "Middle-aged Adult (40-49 years)"
        else:
            return "Mature Adult (50-64 years)"
    else:
        # Senior category with nested conditions
        if age <= 74:
            return "Senior (65-74 years)"
        elif age <= 89:
            return "Elderly (75-89 years)"
        else:
            return "Very Elderly (90+ years)"


def classify_age_simple(age):
    """
    A simpler version of age classification with basic nested conditionals.
    
    Args:
        age (int): The age to classify
    
    Returns:
        str: The age group classification
    """
    if age < 0:
        return "Invalid age"
    elif age < 13:
        return "Child"
    elif age < 20:
        return "Teenager"
    elif age < 65:
        if age < 40:
            return "Young Adult"
        else:
            return "Middle-aged Adult"
    else:
        return "Senior"


# Main execution
if __name__ == "__main__":
    # Get age from user input
    age = int(input("Enter your age: "))
    
    # Classify using detailed nested conditionals
    classification = classify_age_group(age)
    print(f"\nDetailed Classification: {classification}")
    
    # Classify using simple nested conditionals
    simple_classification = classify_age_simple(age)
    print(f"Simple Classification: {simple_classification}")
    
    # Display all age groups for reference
    print("\n" + "="*50)
    print("Age Group Reference:")
    print("="*50)
    test_ages = [1, 4, 7, 10, 14, 17, 25, 35, 45, 55, 70, 80, 95]
    for test_age in test_ages:
        result = classify_age_group(test_age)
        print(f"Age {test_age:3d}: {result}")

