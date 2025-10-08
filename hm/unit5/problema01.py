"""
1. Să se determine dacă trei numere reale a, b şi c pot reprezenta
laturile unui triunghi. Dacă da, să se determine perimetrul său,
altfel să se afişeze un mesaj corespunzător.
"""

def is_triangle(a, b, c):
    if a + b > c and a + c > b and b + c > a:
        return True
    else:
        return False

def main():
    a = float(input("Enter the first side: "))
    b = float(input("Enter the second side: "))
    c = float(input("Enter the third side: "))
    
    is_triangle_result = is_triangle(a, b, c)
    if is_triangle_result:
        print(f"The sides can represent a triangle! Here's the perimeter: {a + b + c}")
    else:
        print("The sides can't represent a triangle")

if __name__ == "__main__":
    main()