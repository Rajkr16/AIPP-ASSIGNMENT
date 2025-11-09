def score_job_applicant(applicant_data):
    """
    Score a job applicant based on multiple features.
    
    Args:
        applicant_data (dict): Dictionary containing applicant information with keys:
            - name (str): Applicant's name
            - years_experience (int/float): Years of relevant work experience
            - education_level (str): Education level (e.g., 'High School', 'Bachelor', 'Master', 'PhD')
            - skills (list): List of relevant skills
            - certifications (list): List of certifications
            - portfolio_projects (int): Number of portfolio projects
            - github_commits (int): Number of GitHub commits (optional, for technical roles)
            - interview_score (float): Interview performance score (0-100)
            - reference_rating (float): Reference rating (0-10)
    
    Returns:
        tuple: (total_score, breakdown_dict, recommendation)
            - total_score (float): Overall score out of 100
            - breakdown_dict (dict): Score breakdown by category
            - recommendation (str): Hiring recommendation
    """
    
    # Initialize scoring weights (sum should be reasonable, will normalize to 100)
    weights = {
        'experience': 25,      # 25% weight
        'education': 20,       # 20% weight
        'skills': 20,          # 20% weight
        'certifications': 10,  # 10% weight
        'portfolio': 10,       # 10% weight
        'interview': 10,       # 10% weight
        'references': 5        # 5% weight
    }
    
    breakdown = {}
    
    # 1. Experience Score (0-25 points)
    years_exp = applicant_data.get('years_experience', 0)
    if years_exp >= 10:
        exp_score = 25
    elif years_exp >= 5:
        exp_score = 20
    elif years_exp >= 3:
        exp_score = 15
    elif years_exp >= 1:
        exp_score = 10
    else:
        exp_score = 5
    breakdown['experience'] = exp_score
    
    # 2. Education Score (0-20 points)
    education = applicant_data.get('education_level', '').lower()
    if 'phd' in education or 'doctorate' in education:
        edu_score = 20
    elif 'master' in education:
        edu_score = 18
    elif 'bachelor' in education:
        edu_score = 15
    elif 'associate' in education or 'diploma' in education:
        edu_score = 10
    elif 'high school' in education:
        edu_score = 5
    else:
        edu_score = 0
    breakdown['education'] = edu_score
    
    # 3. Skills Score (0-20 points)
    skills = applicant_data.get('skills', [])
    num_skills = len(skills)
    # More skills = higher score, capped at 20
    if num_skills >= 10:
        skills_score = 20
    elif num_skills >= 7:
        skills_score = 18
    elif num_skills >= 5:
        skills_score = 15
    elif num_skills >= 3:
        skills_score = 12
    elif num_skills >= 1:
        skills_score = 8
    else:
        skills_score = 0
    breakdown['skills'] = skills_score
    
    # 4. Certifications Score (0-10 points)
    certifications = applicant_data.get('certifications', [])
    num_certs = len(certifications)
    if num_certs >= 5:
        cert_score = 10
    elif num_certs >= 3:
        cert_score = 8
    elif num_certs >= 2:
        cert_score = 6
    elif num_certs >= 1:
        cert_score = 4
    else:
        cert_score = 0
    breakdown['certifications'] = cert_score
    
    # 5. Portfolio Projects Score (0-10 points)
    portfolio = applicant_data.get('portfolio_projects', 0)
    if portfolio >= 10:
        portfolio_score = 10
    elif portfolio >= 5:
        portfolio_score = 8
    elif portfolio >= 3:
        portfolio_score = 6
    elif portfolio >= 1:
        portfolio_score = 4
    else:
        portfolio_score = 0
    breakdown['portfolio'] = portfolio_score
    
    # 6. Interview Score (0-10 points, based on interview_score out of 100)
    interview_score_raw = applicant_data.get('interview_score', 0)
    # Convert 0-100 scale to 0-10 points
    interview_score = (interview_score_raw / 100) * 10
    breakdown['interview'] = round(interview_score, 2)
    
    # 7. Reference Rating Score (0-5 points, based on reference_rating out of 10)
    ref_rating = applicant_data.get('reference_rating', 0)
    # Convert 0-10 scale to 0-5 points
    ref_score = (ref_rating / 10) * 5
    breakdown['references'] = round(ref_score, 2)
    
    # Calculate total score (sum of all categories)
    total_score = sum(breakdown.values())
    
    # Generate recommendation
    if total_score >= 80:
        recommendation = "Highly Recommended - Strong candidate"
    elif total_score >= 70:
        recommendation = "Recommended - Good candidate"
    elif total_score >= 60:
        recommendation = "Consider - Acceptable candidate"
    elif total_score >= 50:
        recommendation = "Maybe - Below average candidate"
    else:
        recommendation = "Not Recommended - Weak candidate"
    
    return total_score, breakdown, recommendation


def display_applicant_score(applicant_data):
    """
    Display formatted scoring results for an applicant.
    
    Args:
        applicant_data (dict): Applicant data dictionary
    """
    total_score, breakdown, recommendation = score_job_applicant(applicant_data)
    
    print(f"\n{'='*60}")
    print(f"Applicant: {applicant_data.get('name', 'Unknown')}")
    print(f"{'='*60}")
    print(f"\nTotal Score: {total_score:.2f}/100")
    print(f"\nScore Breakdown:")
    print("-" * 60)
    for category, score in breakdown.items():
        print(f"  {category.capitalize():20s}: {score:6.2f} points")
    print("-" * 60)
    print(f"\nRecommendation: {recommendation}")
    print(f"\n{'='*60}\n")


def get_user_input():
    """
    Get applicant information from user input.
    
    Returns:
        dict: Applicant data dictionary
    """
    applicant_data = {}
    
    print("\n" + "="*60)
    print("ENTER APPLICANT INFORMATION")
    print("="*60)
    
    # Name
    applicant_data['name'] = input("\nEnter applicant name: ").strip()
    if not applicant_data['name']:
        applicant_data['name'] = 'Unknown'
    
    # Years of Experience
    while True:
        try:
            years_exp = input("Enter years of experience (e.g., 5, 2.5): ").strip()
            applicant_data['years_experience'] = float(years_exp) if years_exp else 0
            break
        except ValueError:
            print("Invalid input. Please enter a number.")
    
    # Education Level
    print("\nEducation Level Options:")
    print("  1. High School")
    print("  2. Associate/Diploma")
    print("  3. Bachelor")
    print("  4. Master")
    print("  5. PhD/Doctorate")
    
    edu_choice = input("Select education level (1-5) or enter custom: ").strip()
    edu_map = {
        '1': 'High School',
        '2': 'Associate',
        '3': 'Bachelor',
        '4': 'Master',
        '5': 'PhD'
    }
    applicant_data['education_level'] = edu_map.get(edu_choice, edu_choice.title())
    
    # Skills
    print("\nEnter skills (comma-separated, e.g., Python, JavaScript, SQL):")
    skills_input = input("Skills: ").strip()
    if skills_input:
        applicant_data['skills'] = [skill.strip() for skill in skills_input.split(',') if skill.strip()]
    else:
        applicant_data['skills'] = []
    
    # Certifications
    print("\nEnter certifications (comma-separated, or press Enter for none):")
    certs_input = input("Certifications: ").strip()
    if certs_input:
        applicant_data['certifications'] = [cert.strip() for cert in certs_input.split(',') if cert.strip()]
    else:
        applicant_data['certifications'] = []
    
    # Portfolio Projects
    while True:
        try:
            portfolio = input("\nEnter number of portfolio projects: ").strip()
            applicant_data['portfolio_projects'] = int(portfolio) if portfolio else 0
            break
        except ValueError:
            print("Invalid input. Please enter a whole number.")
    
    # Interview Score
    while True:
        try:
            interview = input("\nEnter interview score (0-100): ").strip()
            applicant_data['interview_score'] = float(interview) if interview else 0
            if 0 <= applicant_data['interview_score'] <= 100:
                break
            else:
                print("Interview score must be between 0 and 100.")
        except ValueError:
            print("Invalid input. Please enter a number between 0 and 100.")
    
    # Reference Rating
    while True:
        try:
            ref_rating = input("\nEnter reference rating (0-10): ").strip()
            applicant_data['reference_rating'] = float(ref_rating) if ref_rating else 0
            if 0 <= applicant_data['reference_rating'] <= 10:
                break
            else:
                print("Reference rating must be between 0 and 10.")
        except ValueError:
            print("Invalid input. Please enter a number between 0 and 10.")
    
    return applicant_data


# Main program
if __name__ == "__main__":
    print("="*60)
    print("JOB APPLICANT SCORING SYSTEM")
    print("="*60)
    print("\nThis system scores job applicants based on:")
    print("  - Experience (25 points)")
    print("  - Education (20 points)")
    print("  - Skills (20 points)")
    print("  - Certifications (10 points)")
    print("  - Portfolio Projects (10 points)")
    print("  - Interview Score (10 points)")
    print("  - Reference Rating (5 points)")
    print("\nTotal Score: 100 points")
    
    applicants = []
    
    while True:
        # Get applicant data from user
        applicant_data = get_user_input()
        
        # Display score for this applicant
        display_applicant_score(applicant_data)
        
        # Add to list for batch operations
        applicants.append(applicant_data)
        
        # Ask if user wants to enter another applicant
        while True:
            continue_choice = input("Do you want to score another applicant? (y/n): ").strip().lower()
            if continue_choice in ['y', 'yes', 'n', 'no']:
                break
            else:
                print("Please enter 'y' for yes or 'n' for no.")
        
        if continue_choice in ['n', 'no']:
            break
    
    # Summary if multiple applicants
    if len(applicants) > 1:
        print("\n" + "="*60)
        print("SUMMARY - ALL APPLICANTS")
        print("="*60)
        print(f"\nTotal Applicants Scored: {len(applicants)}")
        print("\nApplicant Scores:")
        print("-" * 60)
        
        # Sort by score (highest first)
        scored_applicants = []
        for applicant in applicants:
            total_score, _, recommendation = score_job_applicant(applicant)
            scored_applicants.append((applicant['name'], total_score, recommendation))
        
        scored_applicants.sort(key=lambda x: x[1], reverse=True)
        
        for i, (name, score, recommendation) in enumerate(scored_applicants, 1):
            print(f"{i}. {name:30s} - Score: {score:6.2f}/100 - {recommendation}")
        
        print("-" * 60)
        
        # Find highest and lowest
        if scored_applicants:
            highest = scored_applicants[0]
            lowest = scored_applicants[-1]
            print(f"\nHighest Score: {highest[0]} - {highest[1]:.2f}/100")
            print(f"Lowest Score: {lowest[0]} - {lowest[1]:.2f}/100")
    
    print("\n" + "="*60)
    print("Thank you for using the Job Applicant Scoring System!")
    print("="*60 + "\n")

