class BankAccount:
    """
    A BankAccount class that represents a bank account with basic operations.
    
    Attributes:
        account_balance (float): The current balance in the account
        account_number (str): Unique identifier for the account (optional)
    """
    
    def __init__(self, initial_balance=0.0, account_number=None):
        """
        Initialize a new BankAccount instance.
        
        Args:
            initial_balance (float): The initial balance for the account (default: 0.0)
            account_number (str): Optional account number identifier
        """
        # Initialize the account balance with the provided initial balance
        self.account_balance = initial_balance
        # Store the account number if provided
        self.account_number = account_number
        
        # Validate that initial balance is not negative
        if initial_balance < 0:
            raise ValueError("Initial balance cannot be negative")
    
    def deposit(self, amount):
        """
        Deposit money into the account.
        
        Args:
            amount (float): The amount to deposit (must be positive)
            
        Returns:
            float: The new balance after deposit
            
        Raises:
            ValueError: If the deposit amount is negative or zero
        """
        # Validate that the deposit amount is positive
        if amount <= 0:
            raise ValueError("Deposit amount must be positive")
        
        # Add the amount to the current balance
        self.account_balance += amount
        
        # Return the updated balance
        return self.account_balance
    
    def withdraw(self, amount):
        """
        Withdraw money from the account.
        
        Args:
            amount (float): The amount to withdraw (must be positive)
            
        Returns:
            float: The new balance after withdrawal
            
        Raises:
            ValueError: If the withdrawal amount is negative or zero
            ValueError: If there are insufficient funds
        """
        # Validate that the withdrawal amount is positive
        if amount <= 0:
            raise ValueError("Withdrawal amount must be positive")
        
        # Check if there are sufficient funds
        if amount > self.account_balance:
            raise ValueError(f"Insufficient funds. Available balance: {self.account_balance}")
        
        # Subtract the amount from the current balance
        self.account_balance -= amount
        
        # Return the updated balance
        return self.account_balance
    
    def balance(self):
        """
        Get the current balance of the account.
        
        Returns:
            float: The current account balance
        """
        # Return the current account balance
        return self.account_balance
    
    def __str__(self):
        """
        String representation of the BankAccount.
        
        Returns:
            str: A formatted string with account information
        """
        account_info = f"Account Number: {self.account_number}" if self.account_number else "Account Number: Not specified"
        return f"BankAccount({account_info}, Balance: ${self.account_balance:.2f})"
    
    def __repr__(self):
        """
        Official string representation of the BankAccount.
        
        Returns:
            str: A string representation that can be used to recreate the object
        """
        return f"BankAccount(initial_balance={self.account_balance}, account_number={self.account_number!r})"


# Example usage and testing
if __name__ == "__main__":
    # Create a new bank account with initial balance of $100
    account = BankAccount(initial_balance=100.0, account_number="ACC001")
    print(f"Initial account: {account}")
    print(f"Current balance: ${account.balance():.2f}\n")
    
    # Deposit money
    print("Depositing $50...")
    account.deposit(50.0)
    print(f"Balance after deposit: ${account.balance():.2f}\n")
    
    # Withdraw money
    print("Withdrawing $30...")
    account.withdraw(30.0)
    print(f"Balance after withdrawal: ${account.balance():.2f}\n")
    
    # Try to withdraw more than available (will raise an error)
    try:
        print("Attempting to withdraw $200...")
        account.withdraw(200.0)
    except ValueError as e:
        print(f"Error: {e}\n")
    
    # Final balance
    print(f"Final balance: ${account.balance():.2f}")
    
    # Example with user input
    print("\n" + "="*50)
    print("Interactive Bank Account Demo")
    print("="*50)
    
    # Create a new account
    user_account = BankAccount(initial_balance=0.0)
    print(f"\nNew account created. Initial balance: ${user_account.balance():.2f}")
    
    # Get user input for operations
    while True:
        print("\nOptions:")
        print("1. Deposit")
        print("2. Withdraw")
        print("3. Check Balance")
        print("4. Exit")
        
        choice = input("\nEnter your choice (1-4): ").strip()
        
        if choice == "1":
            try:
                amount = float(input("Enter deposit amount: $"))
                new_balance = user_account.deposit(amount)
                print(f"Deposit successful! New balance: ${new_balance:.2f}")
            except ValueError as e:
                print(f"Error: {e}")
        
        elif choice == "2":
            try:
                amount = float(input("Enter withdrawal amount: $"))
                new_balance = user_account.withdraw(amount)
                print(f"Withdrawal successful! New balance: ${new_balance:.2f}")
            except ValueError as e:
                print(f"Error: {e}")
        
        elif choice == "3":
            print(f"Current balance: ${user_account.balance():.2f}")
        
        elif choice == "4":
            print("Thank you for using the bank account system!")
            break
        
        else:
            print("Invalid choice. Please try again.")

