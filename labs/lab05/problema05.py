"""
5. Să se elaboreze un program care afișează numărul de cifre a unui număr.
"""

def main(n: int) -> int:
    i = 0

    if n == 0:
        print("There is 1 digit in your number.")
        return None

    while n >= 1:
        n //= 10
        i += 1
            
    print(f"There {"is" if i == 1 else "are"} {i} digits in your number.")

if __name__ == "__main__":
    main(int(input("Enter a number: ")))