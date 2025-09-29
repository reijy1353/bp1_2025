"""
12. Este dat un număr natural N. Să se elaboreze un program care calculează câte ore,
minute, secunde sunt în:
    a) n zile (o zi = 24 ore);
    b) n săptămâni (o săptămână = 7 zile);
    c) luna mai.
"""

def timpul():

    # Getting the data
    n = int(input("Enter a natural number: "))

    # Check if n is natural
    if not n >= 0:
        raise ValueError("n should be greater than 0")

    # Days in the fifth month (may) = 31, using for "c)"
    may_days = 31

    # Make calculus
    a_hours, a_minutes, a_seconds = n * 24, (n * 24) * 60, (n * 24) * 3600
    b_hours, b_minutes, b_seconds = (n * 7) * 24, ((n * 7) * 24) * 60, ((n * 7) * 24) * 3600
    c_hours, c_minutes, c_seconds = may_days * 24, (may_days * 24) * 60, (may_days * 24) * 3600

    # Print the results
    print(f"a) {a_hours}h {a_minutes}m {a_seconds}s")
    print(f"b) {b_hours}h {b_minutes}m {b_seconds}s")
    print(f"c) {c_hours}h {c_minutes}m {c_seconds}s")

if __name__ == "__main__":
    timpul()