"""Să se determine aria unui trapez care are baza mică b1, baza
mare b2 şi înălţimea h."""

# Exception in case the smaller base is bigger than the "big" base
class SmallBaseBiggerThanTheBigOne(Exception): pass

# Exception in case it's not a trapezoid
class NotATrapezoid(Exception): pass

# Get the initial data
b1 = float(input("b1 = "))
b2 = float(input("b2 = "))

# Check if it's actually a trapezoid
if b1 == b2:
    raise(NotATrapezoid)

# That check could be eliminated, because we don't care which is bigger (it could a reverse trapezoid)
# Check if b1 is actually smaller than b2
if b1 > b2:
    raise(SmallBaseBiggerThanTheBigOne)

# Get the rest of the data
h = float(input("h = "))

# Get the surface of the trapezoid
surface = ((b1 + b2) * h) / 2

# Print the results (with just 2 digits after the dot e.g. -> .50)
print(f"And the surface of that trapezoid is {surface:.2f}")