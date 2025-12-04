"""
10. Se citește un text de cel mult 255 de caractere, format din litere mici ale alfabetului
englez. Scrieți un program care verifică dacă șirul de caractere este format dintr-un
număr egal de consoane și vocale.
"""

def main():
    s = input("Give a string (max length = 255): ")
    if len(s) > 255: return "The text is too big."

    vowels_list = 'aeiou'
    vowels = 0
    consonants = 0

    for i in s:
        if i in vowels_list: vowels += 1
        else: consonants += 1

    return vowels == consonants

if __name__ == "__main__":
    if main(): print("The vowels and consonats count are equal.")
    else: print("The count of vowels and consonants isn't equal.")