"""
8. Să se elaboreze un program care să citească un număr X natural din exact 3 cifre și
să determine:
    - dacă suma cifrelor numărului X reprezintă un număr din exact 2 cifre;
    - dacă produsul cifrelor numărului X reprezintă un număr din exact 3 cifre;
    - dacă produsul cifrelor numărului X este mai mare decât însuși numărul X;
    - dacă suma cifrelor numărului X este divizibilă cu numărul Y.
"""

def x_on_the_loose(x, y):
    first, second = divmod(x, 100)
    second, last = divmod(second, 10)
    
    # dacă suma cifrelor numărului X reprezintă un număr din exact 2 cifre;
    sum = first + second + last
    if sum >= 10 and sum <= 99:
        print("1. X's sum of digits is a 2 digit number.")
    else: print("1. NONE")
    
    # dacă produsul cifrelor numărului X reprezintă un număr din exact 3 cifre;
    prod = first * second * last
    if prod >= 100 and prod <= 999:
        print("2. X's prod of digits is a 3 digit number.")
    else: print("2. NONE")

    # dacă produsul cifrelor numărului X este mai mare decât însuși numărul X;
    if prod > x:
        print("3. X's prod of digist is bigger than X itself.")
    else: print("3. NONE")

    # dacă suma cifrelor numărului X este divizibilă cu numărul Y.
    if sum % y == 0:
        print("4. X's sum of digits is perfectly divided by Y.")
    else: print("4. NONE")

def main():
    x = int(input("x = "))
    if x < 100 and x > 999:
        print("x isn't a number made of 3 digits")
        return
    y = int(input("y = "))

    x_on_the_loose(x, y)
    
if __name__ == "__main__":
    main()