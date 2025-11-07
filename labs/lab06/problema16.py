"""
16. Să se elaboreze o procedură care determină distanța dintre două puncte A(x1,y1) și
B(x2,y2) și coordonatele mijlocului acestui segment C(x,y).
"""

def get_distance(a: tuple, b: tuple):
    ab = (b[0]-a[0], b[1]-a[1])
    return (ab[0]**2 + ab[1]**2)**(1/2)

def get_midst(a: tuple, b: tuple):
    x_sum = a[0] + b[0]
    y_sum = a[1] + b[1]
    return (x_sum/2, y_sum/2)

def main():
    print("--- hint: enter the coordinates like that: 'x y' ---")
    a = tuple[int, int](map(int, input("Type the coordintates for A: ").split(" ")))
    b = tuple[int, int](map(int, input("Type the coordintates for B: ").split(" "))) 

    distance = get_distance(a, b)
    midst = get_midst(a, b)
    print(f"\nThe distand would be {distance:.02f}")
    print(f"The midsts of your segment is {midst}")

if __name__ == "__main__":
    main()