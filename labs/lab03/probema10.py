"""
10.Se introduce un număr din intervalul 1..10 care reprezintă nota la purtare a elevului.
Să se afișeze caracterizarea verbală a notei (1..4 - nesatisfăcătoare; 5, 6 -
satisfăcătoare; 7, 8 - bună; 9, 10 - exemplară).
"""

def main():
    # Get nota var and check if it's in [1, 10] interval
    nota = int(input("Type your grade: "))
    if not 0 < nota <= 10:
        print("Your grade should be in this interval [1, 10]")

    # Use match-case to tell the user about his grade
    match nota:
        case 1 | 2 | 3 | 4:
            print("You should work harder!!!")
        case 5 | 6:
            print("It's okay.")
        case 7 | 8:
            print("Good.")
        case 9 | 10:
            print("Great!")

if __name__ == "__main__":
    main()