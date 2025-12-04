"""
10. Se introduce un număr natural n. Să se elaboreze un program care determină cifra de
ordin inferior și superior a unui număr introdus de la tastatură.
"""

def main(n: int):
    inferior = n % 10
    while n >= 10:
        n //= 10
        
    print(f"Superior: {n}, Inferior: {inferior}.")
    

if __name__ == "__main__":
    main(int(input("Enter a number: ")))