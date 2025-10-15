ops = {
    "+": lambda a, b: a + b,
    "-": lambda a, b: a - b,
    "*": lambda a, b: a * b,
    "/": lambda a, b: a / b
}

n1 = int(input("Input the first number: "))
n2 = int(input("Input the second number: "))
op = input("Input a operation (+-*/): ")

try:
    result = ops[op](n1, n2)
    print(f"And the result is: {result}")
except KeyError: print("Invalid operation")
except ZeroDivisionError: print("You can't divide by zero.")

