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

    divided = False
    for i in range(2, n//2+1): 
        if n % i == 0:
            divided = True
            break
    
    return divided

def quit(is_composite: bool):
    return "Congrats! Your number is composite!" if is_composite else "You've given me a non composite number."

def main():
    n = get_number()
    print(quit(is_composite(n)))

if __name__ == "__main__":
    main()