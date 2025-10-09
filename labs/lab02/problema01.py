"""
1. Să se elaboreze un program care să citească de la tastatură trei valori numerice a, b, c
şi apoi să afișeze pe ecran cea mai mare diferență dintre oricare două valori date.

Exemplu: pentru a = 100, b = 15, c = 105 se va afișa 90.
"""

def biggest_diff(a, b, c):
    # Biggest difference for a
    a_b = a - b
    a_c = a - c
    max_a_diff = a_c if a_c > a_b else a_b

    # Biggest difference for b
    b_a = b - a
    b_c = b - c
    max_b_diff = b_a if b_a > b_c else b_c
    
    # Biggest difference for c
    c_a = c - a
    c_b = c - b
    max_c_diff = c_a if c_a > c_b else c_b

    if max_a_diff >= max_b_diff and max_a_diff >= max_c_diff:
        largest = max_a_diff
    elif max_b_diff >= max_a_diff and max_b_diff >= max_c_diff:
        largest = max_b_diff
    else:
        largest = max_c_diff
        
    print(f"The largest difference between those 3 variables is: {largest}")
    
if __name__ == "__main__":
    a = int(input("a = "))
    b = int(input("b = "))
    c = int(input("c = "))
    
    biggest_diff(a, b, c)
    