"""Să se elaboreze un algoritm care citeşte de la tastatură un număr
natural, format din 4 cifre şi determină suma primelor 2 cifre a
acestui număr şi suma ultimelor două cifre ale acestui număr."""

# Get the number
number = int(input("Enter a 4 digit number: "))

# Get first two and last numbers
first_two, last_two = divmod(number, 100)

# Get the sum of first and last two numbers
first_two_sum = sum(divmod(first_two, 10))
last_two_sum = sum(divmod(last_two, 10))

# Print the results
print(f"The sum of first two is {first_two_sum}, and here's of the last two {last_two_sum}.")