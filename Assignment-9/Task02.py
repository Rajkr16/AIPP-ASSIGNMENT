from dataclasses import dataclass, field  # Import dataclass utilities for concise data models

# /d:/AIPP/Assignment-9/Task02.py

@dataclass  # Automatically generates __init__, __repr__, etc., based on fields
class sru_student:
    """
    Simple SRU student model with:
    - name: student name
    - roll_no: roll number
    - hostel_status: True if hosteller, False if day scholar
    - base_fee: academic fee
    - hostel_fee: hostel fee (applied only if hostel_status is True)
    """
    name: str                     # Student's full name
    roll_no: str                  # Unique roll number/ID
    hostel_status: bool           # True if student is a hosteller, else False
    base_fee: float               # Academic/tuition fee
    hostel_fee: float = 0.0       # Hostel fee (used only when hostel_status is True)
    fee_due: float = field(init=False)  # Computed post-init; not set by caller

    def __post_init__(self) -> None:  # Runs automatically after dataclass __init__
        if self.base_fee < 0 or self.hostel_fee < 0:  # Validate that fees are non-negative
            raise ValueError("Fees cannot be negative.")  # Guard against invalid input
        # Compute total due: base fee + hostel fee only if the student is a hosteller
        self.fee_due = self.base_fee + (self.hostel_fee if self.hostel_status else 0.0)

    def fee_update(self, payment: float) -> float:
        """
        Register a payment and return remaining due.
        """
        if payment < 0:  # Reject negative payments
            raise ValueError("Payment cannot be negative.")
        # Subtract payment from due; never let due go below zero
        self.fee_due = max(0.0, self.fee_due - payment)
        return self.fee_due  # Return updated remaining due

    def display_details(self) -> None:
        """
        Print student details and current fee due.
        """
        print(f"Name          : {self.name}")  # Show student's name
        print(f"Roll No.      : {self.roll_no}")  # Show roll number
        # Show hostel status in human-readable form
        print(f"Hostel Status : {'Hosteller' if self.hostel_status else 'Day Scholar'}")
        print(f"Fee Due       : ₹{self.fee_due:.2f}")  # Show current outstanding amount

if __name__ == "__main__":  # Execute demo only when run as a script
    # Example usage
    # Hosteller: base fee + hostel fee
    name1 = input("Enter name for hosteller student: ").strip() or "Anita"  # Get name or default
    # Instantiate a hosteller student; __post_init__ validates fees and computes fee_due
    s1 = sru_student(
        name=name1,            # Student's name from user input
        roll_no="22CS101",     # Unique roll number identifier
        hostel_status=True,    # Hosteller => hostel_fee will be included
        base_fee=50000.0,      # Academic fee component
        hostel_fee=30000.0     # Hostel fee component (applied because hostel_status is True)
    )
    s1.display_details()  # Print initial details and total due
    print("\nPayment of ₹10,000 processed...")  # Simulate a payment event
    s1.fee_update(10000.0)  # Apply payment and update due
    s1.display_details()  # Print updated details

    print("\n---------------------------\n")  # Visual separator

    # Day scholar: base fee only
    name2 = input("Enter name for day scholar student: ").strip() or "Rahul"  # Get name or default
    # For a day scholar, hostel_fee is ignored because hostel_status=False
    s2 = sru_student(
        name=name2,
        roll_no="22EC057",
        hostel_status=False,   # Day scholar => hostel_fee will not be added
        base_fee=45000.0,
        hostel_fee=25000.0     # Provided but ignored due to hostel_status=False
    )
    s2.display_details()  # Print initial details and total due
    print("\nPayment of ₹20,000 processed...")  # Simulate a payment event
    s2.fee_update(20000.0)  # Apply payment and update due
    s2.display_details()  # Print updated details