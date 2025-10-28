"""
10. Să se elaboreze un program care verifică dacă un număr natural nenul dat este
„perfect”, adică este egal cu suma divizorilor săi proprii, inclusiv 1. Exemplu:
6=1+2+3 este număr perfect.
"""

# n > 0 (int)

# max divizor = n/2
# for -- if n % i == 0 list.append(), then sum list, and check, if yes return True, not return False

perfect_divisors = []
def perfect_numbers(n):
    # * for i in range(1, n//2+1):
    #     if n % i == 0:
    #         perfect_divisors.append(i)
            
    # return True if sum(perfect_divisors) == n else False

    # * alternative
    # return True if sum([i for i in range(1, n//2+1) if n % i == 0]) == n else False

    # * without using lists
    sum = 0
    for i in range(1, n//2+1):
        if n % i == 0:
            sum += i
        
    return True if sum == n else False

def main():
    n = int(input("Please enter a natural number >0: "))
    if not n > 0: print("Number isn't > 0")

    if perfect_numbers(n): print("The number is a PERFECT one.")
    else: print("Unfortunately the number isn't a PERFECT one, try another one...")

if __name__ == "__main__":
    main()
