"""
12. De realizat un program de afișare a tuturor numerelor de 2 cifre, suma cifrelor cărora
este egală cu un număr dat.
"""

def main():
    n = int(input("Type a number: "))
    print("All 2 digit numbers, which digits are equal to n:")
    for i in range(10, 100):
        if i // 10 + i % 10 == n:
            print(i)
    
if __name__ == "__main__":
    main()