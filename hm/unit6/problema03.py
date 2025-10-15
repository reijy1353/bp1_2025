"""
3. Să se elaboreze algoritmul care citeşte de la tastatură 10 numere
întregi şi afişează numărul celor pozitive, folosind construcţia
While.
"""

def get_positives():
    """Lazy to type the explanation"""

    # Flag for tracking all the positive numbers (positive_numbers)\
        # and max number entries (i)
    positive_numbers = 0
    i = 0

    # The while statement
    while i < 10:
        # Check if the numbers are valid
        try:
            n = int(input("Enter a number, please: "))
        except ValueError:
            print("This is not a number, I think so at least...\n")
            continue

        # Check if the number is positive
        if n >= 0:
            positive_numbers += 1
        
        # Incrementing "i"
        i += 1
        
    # Return the results
    return positive_numbers

# main() func, where everything happens
def main():
    pos_numbers = get_positives()
    print(f"There were {pos_numbers} positive numbers in all of your entries.")

# Execute the main() func if it runs from the main file (this one)
if __name__ == "__main__":
    main()