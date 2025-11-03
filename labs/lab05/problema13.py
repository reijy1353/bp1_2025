"""
13. Se citesc numerele naturale până la întâlnirea numărului 0. Să se elaboreze un
program care afișează toate perechile de numere cu proprietatea că al doilea număr
reprezintă restul împărțirii primului număr la suma cifrelor sale.
"""

def check_if_broken(n):
    """Checking if a number is 0, to make sure to break the loop."""
    return n == 0

def main():
    sum_digits = 0
    while True:
        # Gettign the data from the user [and breaking the loop if one's zero ("0")]
        n1 = int(input("\nEnter the first number: "))
        if check_if_broken(n1): break
        n2 = int(input("Enter the second number: "))
        if check_if_broken(n2): break

        # Getting the digits from the first number
        n1_temp = n1
        while n1_temp >= 1:
            sum_digits += n1_temp % 10
            n1_temp //= 10 
        
        # Checking if n2 = n1 % n1's digits' sum
        if n2 == n1 % sum_digits:
            # Printing out the results
            print(f"\nn2 ({n2}) is equal to n1 ({n1}) % its digits' sum ({sum_digits}).")
        else: print(f"\nThey weren't equal, continuing... (n1 % its digits' sum = {n1 % sum_digits}, but n2 = {n2})")

if __name__ == "__main__":
    main()