"""
10. Să se elaboreze un program care citește de la tastatură un număr natural nenul n cu
exact 6 cifre și, folosind apeluri ale funcției VERIF, verifică dacă n are primele trei
cifre impare. Programul afișează pe ecran mesajul DA în caz afirmativ și mesajul
NU în caz contrar
"""

def verif(n: int = None) -> bool:
	return all([True if int(i) % 2 == 1 else False for i in str(n)[:3]])

def main():
    n = int(input("Gimme a number: "))

    if n < 0 or n >= 1000000: return None
 
    print(f"And your result is... {verif(n)}")
 
if __name__ == "__main__":
    main()