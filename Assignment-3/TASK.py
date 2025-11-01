# Simple billing calculator: reads PU (price/unit), CU (consumed units), customer type,
# applies default or custom charges and prints EC, FC, CC, ED and total bill.

def get_float(prompt, default=None):
    while True:
        s = input(f"{prompt}" + (f" [{default}]" if default is not None else "") + ": ").strip()
        if s == "" and default is not None:
            return float(default)
        try:
            v = float(s)
            if v < 0:
                print("Enter a non-negative number.")
                continue
            return v
        except ValueError:
            print("Invalid number.")

def choose_customer_type():
    types = {"residential", "commercial", "industrial"}
    while True:
        t = input("Enter customer type (residential/commercial/industrial) [residential]: ").strip().lower()
        if t == "":
            return "residential"
        if t in types:
            return t
        print("Invalid type. Choose residential, commercial or industrial.")

def main():
    print("Electricity bill calculator")
    pu = get_float("Price per unit (PU)", default="1.0")
    cu = get_float("Units consumed (CU)", default="0")
    ctype = choose_customer_type()

    # Default charges by customer type (can be overridden)
    defaults = {
        "residential": {"FC": 50.0, "CC": 20.0, "duty_pct": 5.0},
        "commercial":  {"FC": 100.0, "CC": 30.0, "duty_pct": 10.0},
        "industrial":  {"FC": 150.0, "CC": 50.0, "duty_pct": 12.0},
    }

    print("Press Enter to accept defaults for charges or enter custom values.")
    fc = get_float("Fixed Charges (FC)", default=str(defaults[ctype]["FC"]))
    cc = get_float("Customer Charges (CC)", default=str(defaults[ctype]["CC"]))
    duty_pct = get_float("Electricity Duty percent (ED %)", default=str(defaults[ctype]["duty_pct"]))

    # Calculations
    ec = pu * cu
    ed = ec * (duty_pct / 100.0)
    bill = ec + fc + cc + ed

    # Print results
    print("\n--- Bill Details ---")
    print(f"EC (Energy Charges)         : {ec:.2f}")
    print(f"FC (Fixed Charges)          : {fc:.2f}")
    print(f"CC (Customer Charges)       : {cc:.2f}")
    print(f"ED (Electricity Duty)       : {ed:.2f}")
    print(f"Total Bill                  : {bill:.2f}")

if __name__ == "__main__":
    main()