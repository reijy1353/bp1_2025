"""
1. Se citește un text de cel mult 255 caractere. Scrieți un program care înlocuiește toate
vocalele din text cu ‘*’. Exemplu: ‘abedi’ -> ‘*b*d*’
"""

def main():
    s = input("Give a string (max length = 255): ")
    if len(s) > 255: return "The text is too big."

    vowels_list = 'aeiou'

    return f"Response: {"".join([i if i in vowels_list else "*" for i in s])}"

if __name__ == "__main__":
    print(main())