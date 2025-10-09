"""
2. Afișați decada căreia îi aparține o anumită zi dintr-o lună oarecare:
    1..10 - decada I
    11..20 - decada II
    21..30 - decada III
    31 - decada IV
"""
    
def main():
    zi = int(input("Zi = "))
    if zi < 1 or zi > 31:
        print("Enter a number from 1 to 31 next time (it's a month after all)")
        return

    if 1 <= zi <= 10: print("Decada I")
    elif 11 <= zi <= 20: print("Decada II")
    elif 21 <= zi <= 30: print("Decada III")
    else: print("Decada IV")

if __name__ == "__main__":
    main()