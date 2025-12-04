"""
13. Se citește un text de cel mult 200 de caractere format din cuvinte separate între ele
prin câte un spațiu, care se termină cu caracterul ‘.’. Fiecare cuvânt are cel mult 20
de caractere, doar litere mici ale alfabetului englez. Scrieți un program care afișează
pe linii separate doar cuvintele din textul citit, care conțin cel mult două vocale. Se
consideră vocale: a, e, i, o, u.

Exemplu: ‘pentru examenul se folosesc teste.’
pentru
se
teste
"""

def check_vowel(s: str):
    vowel_count = 0
    for i in 'aeiou':
        if vowel_count:= vowel_count + s.count(i) > 1: return True
    return False

def main():
    s = input("Give a string (max length = 255): ")
    if len(s) > 200: return "The text is too big."

    # Add dot at the end 
    if s[-1] != '.': s = s + "."
    
    # Transform the string to a proper form
    forbidden_chars = "ăîțșâ"
    trans_table = str.maketrans('', '', forbidden_chars)
    print(trans_table)
    s = s.lower().strip().translate(trans_table)

    print(f"Here's your string: {s}")

    # Divide all the words by " " (blank space)
    s = s[:-1].split(' ')
    print(s)

    s = [i for i in s if check_vowel(i)]
    print(f"Your final words are:\n{"\n".join(s)}")

if __name__ == "__main__":
    main()