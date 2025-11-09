class Student:
    def __init__(self, name, age, student_id, course):
        """
        Constructor to initialize Student attributes.
        
        Args:
            name (str): Student's name
            age (int): Student's age
            student_id (str): Student's ID
            course (str): Course name
        """
        self.name = name
        self.age = age
        self.student_id = student_id
        self.course = course
    
    def display_details(self):
        """
        Method to display all student details.
        """
        print("Student Details:")
        print(f"Name: {self.name}")
        print(f"Age: {self.age}")
        print(f"Student ID: {self.student_id}")
        print(f"Course: {self.course}")


# Example usage
if __name__ == "__main__":
    # Get student details from user input
    name = input("Enter student name: ")
    age = int(input("Enter student age: "))
    student_id = input("Enter student ID: ")
    course = input("Enter course: ")
    
    # Create a student object
    student1 = Student(name, age, student_id, course)
    
    # Display student details
    student1.display_details()

