"""
2. Să se determine de ce tip (isoscel, echilateral, dreptunghic) este
un triunghi cu laturile a, b şi c.
"""

def is_triangle(a, b, c):
    return True if a + b > c and a + c > b and b + c > a else False 

def what_type_of_triangle(a, b, c):
    if a == b and a == c and c == b:
        print("It's a Equilateral triangle! (all sides are equal)")
    elif a == b or a == c or b == c:
        print("It's a Isosceles triangle! (2 sides are equal)")
    else:
        print("It's a Scalene triangle! (no equals sides)")
        

def main():
    a = float(input("Enter the first side: "))
    b = float(input("Enter the second side: "))
    c = float(input("Enter the third side: "))

    if is_triangle(a, b, c): what_type_of_triangle(a, b, c)
    else: print("You're not having a triangle here Mister!")

if __name__ == "__main__":
    main()