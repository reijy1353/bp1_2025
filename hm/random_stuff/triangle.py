# Make a class to raise() when not a triangle
class NotATriangle(Exception): pass

def calculate_surface_and_perimeter_of_a_triangle():
    """Here we'll calculate both perimeter and the surface of a triangle"""

    # Getting the 3 side of the triangle
    print("I would like you to write me the a, b and c sides of a triangle (which are positive, not null and float/real)")
    a = float(input("a = "))
    b = float(input("b = "))
    c = float(input("c = "))

    # Checking if it's a triangle
    if not ((a + b > c) and (a + c > b) and (b + c > a)):
        raise(NotATriangle)

    # Calculating the perimeter
    perimeter = a + b + c

    # Calculating the surface (using power 1/2 instead of sqrt() function)
    semi_perimeter = perimeter / 2
    surface = (semi_perimeter*(semi_perimeter-a)*(semi_perimeter-b)*(semi_perimeter-c))**(1/2)

    # Printing the results
    print(f"The perimeter of the triangle is: {perimeter}\nThe surface of the triangle is: {surface}")

# Testing the program
# if __name__ == "__main__":
#     calculate_surface_and_perimeter_of_a_triangle()

# Program (but we repeat it if the user wants to)
if __name__ == "__main__":
    calculate_surface_and_perimeter_of_a_triangle()
    while True:
        response = input("\nWould you like to repeat the program?\n")
        if response == "yes": calculate_surface_and_perimeter_of_a_triangle()
        else: break

