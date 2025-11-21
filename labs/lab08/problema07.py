"""
7. Să se elaboreze un program care completează un vector A cu n caractere citite de la
tastieră și afișează mai întâi elementele de pe pozițiile pare, iar apoi cele de pe poziții 
"""

def main():
    n = int(input("Gimme the length: "))
    a = [int(input(f"{i+1}. Number = ")) for i in range(n)]

    print(f"Odd position: {a[::2]}")
    print(f"Even position{a[1::2]}")

if __name__ == "__main__":
    main()