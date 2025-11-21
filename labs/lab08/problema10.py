"""
10. Să se elaboreze un program care completează un vector A cu n numere naturale citite
de la tastieră și afișează perechile de elemente vecine din vector care au suma
divizibilă cu k (citită de la tastieră).
"""


def main():
        n = int(input("Gimme a number: "))
        a_vector: list[int] = [input(f"{i+1}. Input number: ") for i in range(n)]
        k = int(input("Write down the k variable: "))

        for i in range(len(a_vector)):
            if i < len(a_vector)-1 and int(a_vector[i]) + int(a_vector[i+1]) == k:
                print(f"a_vector[{i}] + a_vector[{i+1}] are equal to K")


if __name__ == "__main__":
    main()