"""
4. Se citește un număr natural X format din exact 4 cifre nenule. Afișați numerele
obținute în următoarele moduri:
    a) schimbând prima cifră cu ultima;
    b) schimbând între ele cifrele din mijloc;
    c) înlocuind cifrele din mijloc cu doi de 0.
"""

def transformarea_numarului():
    
    # Get the number formed of exactly 4 digits
    number = int(input("Please enter a number (4 digits): "))

    # Getting all the digits from the number
    two_digit_left, two_digit_right = divmod(number, 100)
    digit_one, digit_two = two_digit_left // 10, two_digit_left % 10
    digit_three, digit_four = two_digit_right // 10, two_digit_right % 10

    # Results (using f"" string)
    print("Here are the results:")
    print(f"a) {digit_four}{digit_two}{digit_three}{digit_one}")
    print(f"b) {digit_one}{digit_three}{digit_two}{digit_four}")
    print(f"c) {digit_one}00{digit_four}")

    # # Another example (using decimal positions)
    # n_one = digit_four * 1000 + digit_two * 100 + digit_three * 10 + digit_one
    # n_two = digit_one * 1000 + digit_three * 100 + digit_two * 10 + digit_four
    # n_three = digit_one * 100 + digit_two * 10 + digit_three * 100 + digit_four
    # print(f"a) {n_one}")
    # print(f"b) {n_two}")
    # print(f"c) {n_three}")

if __name__ == "__main__":
    transformarea_numarului()