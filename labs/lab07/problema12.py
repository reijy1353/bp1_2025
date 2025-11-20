"""
12. Să se elaboreze un program care citește de la tastatură două numere naturale nenule
de cel mult 4 cifre, a și b (a<b) și, folosind apeluri ale funcției NUMAR, verifică
dacă intervalul [a, b] conține cel puțin un număr prim. Programul va afișa pe ecran,
în caz afirmativ, mesajul DA, iar în caz contrar, mesajul NU
"""

def numar(a: int = 1000, b: int = 1000) -> bool:
    for i in range(a, b+1):
        divisors = [i]
        for j in range(1, (i//2)+1):
            if i % j == 0:
                divisors.append(j)
        
        # print(divisors)
        if len(divisors) == 2:
            return True

    return False

def read_number():
    number = int(input("Gimme a number: "))
    
    if not (0 < number <= 10000):
        print("!Your number isn't in the proper interval, setting up 1000 by default")
        return 1000

    return number

def main():
    a = read_number()
    b = read_number()

    if a > b:
        print("\nA is bigger than B, interchaing them.")
        return numar(b, a)
    elif a == b:
        print("\nYour numbers are equal...")
        return numar(a, b)

    return numar(a, b)
    
if __name__ == "__main__":
    print("DA") if main() else print("NU")