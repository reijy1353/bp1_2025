"""
2. Să se elaboreze un program care completează un vector A cu n numere naturale citite
de la tastieră și determină dacă toate elementele vectorului dat sunt diferite
"""

def main():
    vector_a = []
    n = int(input("Give me the length of your vector: "))
    for _ in range(n):
        c = int(input("Gimme a number: "))
        vector_a.append(c)

    for i in vector_a:
        if vector_a.count(i) > 1:
            return "You have elements that are equal to each other."
    return "None of your elements are equal."

if __name__ == "__main__":
    print(main())