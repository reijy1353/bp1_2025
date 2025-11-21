"""
2. Să se elaboreze un program care completează un vector A cu n numere naturale citite
de la tastieră și ordonează crescător prima jumătate și descrescător cea de a doua
jumătate a vectorului. La final programul afișează pe ecran vectorul obținut.
"""

def main():
    n = int(input("Length: "))
    a = [int(input(f"{i+1}. Gimme a number: ")) for i in range(n)]

    middle = len(a) // 2
    first_half = sorted(a[:middle])
    second_half = sorted(a[middle:], reverse=True)
    a = first_half + second_half

    print(f"Your vector is looking like that: {a}")

if __name__ == "__main__":
    main()