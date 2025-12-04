"""
10. Să se elaboreze un program care completează un vector A cu n numere naturale citite
de la tastieră și determină dacă în vector sunt numere prime.
"""

def is_prime(n: int):
    """Check if a number is prime"""
    if n <= 1: return False
    else:
        for i in range(2, int(n**0.5) + 1):
            if n % i == 0:
                return False
        return True

def main():
    """Main function"""
    vector_a = []
    n = int(input("What's the size of your vector?: "))
    for _ in range(n):
        num = int(input("Gimme a number: "))
        vector_a.append(num)

    for i in vector_a:
        if is_prime(i): return "There is a prime number in your vector."
    return "There are no prime numbers in your vector."
        

if __name__ == "__main__":
    print(main())