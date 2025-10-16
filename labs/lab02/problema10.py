"""
10. Orice sumă de bani S (S>7) poate fi plătită numai cu monede de 3 şi 5 lei. Dat fiind
S>7, scrieți un program care să determine o modalitate de plată a sumei S numai
cu monede de 3 şi 5 lei.
"""

def payment_method(s, method):
    """Some info about this fucntion"""

    # Method 1 (we pay with both)
    # # Make the calculus
    # paid_5, rest = divmod(s, 5)
    # paid_3, rest = divmod(rest, 3)

    # # Print the result
    # print(f"You'll need {paid_5} pieces of 5 coins")
    # print(f"You'll need {paid_3} pieces of 3 coins")
    # print(f"The remaining is {rest}")

    # Method 2 (the right way)
    if method == 5: print(f"You'll need {s//5} coins, you'll be having {s%5} lei debt.")
    else: print(f"You'll need {s//3} coins, you'll be having {s%3} lei debt.")

# Here happens everything
def main():
    # Get the sum (from the user)
    s = int(input("Type the sum you would like to pay: "))
    if s < 8:
        print("The sum should be greater than 7")
        return

    # Fetching the method from the user
    method = int(input("With which coins will you pay (3 or 5): "))
    if method not in [3, 5]:
        print("You only can pay with 3 or 5 lei coins.")
        return

    # The results
    payment_method(s, method)

# Execute the program from main file
if __name__ == "__main__":
    main()