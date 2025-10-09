"""
4. Să se elaboreze un program care să citească de la tastatură două numere reale a și b,
apoi să pună utilizatorului întrebarea: Ce doriți să calculați, media aritmetică sau
geometrică? Dacă se va răspunde prin 1, se va calcula și afișa media aritmetică a
numerelor, iar pentru 2 - media geometrică (numai în cazul numerelor pozitive). Dacă
nu se răspunde prin 1 sau 2 se va afișa 'Răspuns incorect'.
"""

def calcluate_arithmethic_geometric_mean(a, b, response):
    if response == 1:
        print(f"The aritmetic mean is {(a+b)/2:.2f}")
    elif response == 2:
        print(f"The geometric mean is {(a*b)**(1/2):.2f}")

        if not (a >= 0 and b>=0):
            print("Both a and b should be positive numbers.")

def main():
    a = int(input("a = "))
    b = int(input("b = "))

    response = int(input("Type '1' for arithmetic mean and '2' for geometric mean: "))
    
    calcluate_arithmethic_geometric_mean(a, b, response)

if __name__ == "__main__":
    main()