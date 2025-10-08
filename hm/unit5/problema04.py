"""
Să se determine dacă un număr este divizibil cu toate numerele
b1, b2, b3.
"""

def can_you_divide(b1, b2, b3):
    if (b2 != 0 and b3 != 0) and (b1 % b2 == 0 and b1 % b3 == 0):
        print("b1 can be divided by both b2 and b3")
    if (b1 != 0 and b3 != 0) and (b2 % b1 == 0 and b2 % b3 == 0):
        print("b2 can be divided by both b1 and b3")
    if (b1 != 0 and b2 != 0) and (b3 % b1 == 0 and b3 % b2 == 0):
        print("b3 can be divided by both b1 and b2")

def main():
    b1 = int(input("b1 = "))
    b2 = int(input("b2 = "))
    b3 = int(input("b3 = "))

    can_you_divide(b1, b2, b3)

if __name__ == "__main__":
    main()