def evaluate_loan_application(name, gender, annual_income, credit_score):
    # Set threshold values for loan approval
    MIN_INCOME = 30000
    MIN_CREDIT_SCORE = 650
    
    # Store decision factors
    factors = []
    
    # Evaluate based on objective financial criteria only
    if annual_income >= MIN_INCOME:
        factors.append("Income meets minimum requirement")
    else:
        factors.append("Income below minimum requirement")
        
    if credit_score >= MIN_CREDIT_SCORE:
        factors.append("Credit score meets minimum requirement")
    else:
        factors.append("Credit score below minimum requirement")
    
    # Make decision based only on financial factors
    approved = annual_income >= MIN_INCOME and credit_score >= MIN_CREDIT_SCORE
    
    return approved, factors

# Test the system with different applicants
test_cases = [
    ("John", "M", 45000, 700),
    ("Mary", "F", 55000, 620),
    ("Raj", "M", 25000, 680),
    ("Priya", "F", 65000, 750)
]

# Run tests and display results
print("Loan Application Results:")
print("-" * 50)

for name, gender, income, credit_score in test_cases:
    approved, factors = evaluate_loan_application(name, gender, income, credit_score)
    
    print(f"\nApplicant: {name}")
    print(f"Gender: {gender}")
    print(f"Annual Income: ${income:,}")
    print(f"Credit Score: {credit_score}")
    print(f"Loan Status: {'APPROVED' if approved else 'DENIED'}")
    print("Factors considered:")
    for factor in factors:
        print(f"- {factor}")