"""
5. Să se elaboreze un program care afișează numărul de cifre a unui număr.
"""

def main(n: int) -> int:
    i = 0
    while True:
        if n >= 1:
            n //= 10
            i += 1
        else: break
            
    print(f"There are {i} digits in your number.")

if __name__ == "__main__":
    main(int(input("Enter a number: ")))