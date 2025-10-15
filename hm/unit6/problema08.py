"""
8. Să se elaboreze algoritmul care “inversează” un număr întreg.
De exemplu, pentru numărul 1234 să obţinem numărul 4321.
"""

def opposite_number():
    """Return the opposite for any number (e.g., 2020 = 0202 (or 202))"""
    # Method 1 (pretty interesting)
    # return str(n := int(input("Type a number, please: ")))[::-1]

    # Method 2
    # Trying to properly fetch the number
    while True:
        try:
            n = int(input("Enter a number: "))
            break
        except ValueError:
            print("Enter a valid number... please...\n")
            continue

    # Get the reversed number
    reversed_n = ""
    for c in str(abs(n)):
        reversed_n = c + reversed_n

    # Remove the zeroes from the left (if there are)
    reversed_n.lstrip("0")

    # Make sure it return opposite/reverse negative numbers too    
    if n < 0:
        reversed_n = "-" + reversed_n
        
    # Return the result
    return n, reversed_n
        
    
# main() func
def main():
    n, reversed_number = opposite_number()
    print(f"\nThe number: {n}\nIt's opposite is {reversed_number}")

# Executes the program if it's runned from the main file
if __name__ == "__main__":
    main()