"""
13. Să se elaboreze un program care citește de la tastatură un număr natural n (0<n<25),
apoi un șir de n numere naturale nenule cu cel mult 6 cifre și afișează pe ecran
numerele din șir care au suma cifrelor egală cu X, folosind apeluri ale funcției
SUM_CIF.
"""

def sum_cif(numbers: list[int] = [0], x: int = 2) -> int:
    return [
        number for number in numbers
        if sum(int(i) for i in str(number)) == x
    ]

def read_number():
    n = int(input("Gimme the lenght of your number list: "))
    if not (0 < n < 25): 
        print("You should've enter a right number... no worries n = 5 now")
        return 5
    return n

def read_number_list(length: int = 5):
    return [
        n if 0 <= n <= 1000000 else 3939
        for _ in range(length)
        if (n := int(input("Gimme a number: ")))
    ]

def main():
    length = read_number()
    number_list = read_number_list(length)

    if response := sum_cif(number_list, x := int(input("Enter the X number: "))):
        print(response)
        print(f"Here are the next numers of which digits sum equals to X (={x}): {" ".join(str(i) for i in response) if response else 'None'}")

if __name__ == "__main__":
    main()