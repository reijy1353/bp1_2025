"""
13. Să se elaboreze un program care completează doi vectori A și B cu n numere naturale
citite de la tastieră și determină dacă în primul vector A nu există elementele din cel
de al doilea vector B.
"""

def write_to_list(vector: set, length: int):
    for _ in range(length):
        number = int(input("Give me a number: "))
        vector.add(number)

def main():
    n = int(input("Give me the length of vector a and b: "))
    vector_a, vector_b = set(), set()

    print("Get numbers for vector_a")
    write_to_list(vector_a, n)
    print("Get numbers for vector_b")
    write_to_list(vector_b, n)

    vector_a = list[int](vector_a)
    vector_b = list[int](vector_b)
    
    vector_a.extend(vector_b)
    print(vector_a)

    for i in vector_a:
        if vector_a.count(i) > 1:
            return "A number that repeats in both vector a and b exists."
    return "None repeats."

if __name__ == "__main__":
    print(main())
    