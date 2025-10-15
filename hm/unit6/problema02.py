"""
2. Să se elaboreze algoritmul care citeşte numere naturale până la
introducerea numărului 0 şi afişează câte din ele sunt formate
exact din 2 cifre.
"""

def get_two_digit_numbers():
    """Here could be an explanation, but I'm lazy do type something."""

    # Flag to track how many 2digit numbers we'll have
    two_digit_numbers: int = 0

    # The WHILE statement
    while True:
        # Fetching a n number, also making sure it's really a number (int)
        try:
            n = int(input("Please enter a number: "))
        except ValueError:
            print("Please enter a valid number...")
            continue
            
        # Check if n is 0, then finish program, if not, check if n is a 2 digit number
        if n == 0:
            print("Programul a fost finalizat...")
            break
        elif abs(n) // 100 == 0:
            two_digit_numbers += 1

    # Print the results
    print(f"You had {two_digit_numbers} numbers formed of 2 digits.")
            
# The main function, where everything happends
# (actually I don't know why I needed it this time)
def main():
    get_two_digit_numbers()

# Execute the program if it's running from the main file (this file)
if __name__ == "__main__":
    main()