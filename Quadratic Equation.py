# Import complex math module
import cmath

# Take input from the user

a = float(input("Enter First "))
b = float(input("Enter Second "))
c = float(input("Enter Third "))

# Calculate the discriminant
d = (b ** 2) - (4*a*c)

# Find two solutions
sol1 = (-b-cmath.sqrt(d))/(2*a)
sol2 = (-b+cmath.sqrt(d))/(2*a)

print("The solution are {0} and {1}".format(sol1,sol2))
