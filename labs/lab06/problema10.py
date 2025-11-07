"""
10. Să se elaboreze un program, folosind proceduri, pentru reprezentarea și realizarea
următorului meniu:
    - Introducerea numărului;
    - Determinarea dacă numărul este compus;
    - Ieșire din program.
"""

def get_number():
    n = int(input("Please enter a number: "))
    return n

def is_composite(n: int) -> bool:
    if n < 3:
        return False

    divisors = 0
    for i in range(1, n//2+1):
        if n % i == 0:
            divisors += 1
        
        if divisors > 2:
            return True
    
    if divisors < 3:
        return False

def quit(is_composite: bool):
    return "Congrats! Your number is composite!" if is_composite else "You've given me a non composite number."

def main():
    n = get_number()
    print(quit(is_composite(n)))

if __name__ == "__main__":
    main()