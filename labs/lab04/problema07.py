"""
De la tastatură se introduc 10 numere întregi. Să se elaboreze un program care
determină și afișează:
    - numărul celor pozitive și suma lor,
    - media aritmetică а celor negative.
"""

def number_play(n):
    sum_pos = 0
    n_pos = 0
    arithmetic_mean = 0
    n_neg = 0
    for i in range(n):
        n = int(input(f"Enter the {i+1} number: "))
        if n >= 0:
            n_pos += 1
            sum_pos += n
        elif n < 0:
            n_neg += 1
            arithmetic_mean += n

    if n_neg > 0:
        arithmetic_mean = arithmetic_mean / n_neg

    return n_pos, sum_pos, arithmetic_mean


def main():
    n_pos, sum_pos, arithmetic_mean = number_play(10)
    print(f"\n- Count of positive numbers is {n_pos}, and their sum is {sum_pos};")
    print(f"- The arithmetic mean of negative numbers is {arithmetic_mean:.2f}.")

if __name__ == "__main__":
    main()
