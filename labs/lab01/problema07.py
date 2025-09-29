"""
7. Alexandra a economisit S lei și vrea să depoziteze această sumă la o bancă cu o
dobânda de P% pe an, pe un termen de 3 luni. Să se afișeze dobânda obținută de Alexandra
după 3 luni. Valorile S și P sunt numere naturale citite de la tastatură.
"""

from multiprocessing import Value


def banii_alexandrei():

    # Get the data
    s = int(input("What's the sum you have saved?: "))
    p = int(input("What's the interest? (%): "))

    # Make sure s and p are natural
    if not (s >= 0 and (p >= 0 and p <= 100)):
        raise ValueError("s or p should be natural number (and p smaller than 100).")

    # Doing some calculus
    s = s * (p / 100) * (3 / 12)

    # Print results
    print(f"Alex's interest after 3 months will be: {s:.2f}")

if __name__ == "__main__":
    banii_alexandrei()