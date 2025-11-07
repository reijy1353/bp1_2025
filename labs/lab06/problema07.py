"""
7. Să se descrie o procedură care determină dacă un număr este perfect.
"""

def is_perfect(n: int) -> bool:
    divisors = []
    for i in range(1, n//2+1):
        if n % i == 0: divisors.append(i)
    
    return sum(divisors) == n


def main(n: int) -> any:
    return "It is perfect!" if is_perfect(n) else "It isn't perfect :("


if __name__ == "__main__":
    print(main(int(input("Enter a number: "))))