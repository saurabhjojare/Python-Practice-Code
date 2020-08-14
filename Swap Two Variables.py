# Python Program To Swap Two Variables

x = input("Enter Value Of x: ")
y = input("Enter Value Of y: ")

# Create a temporary variable and swap the values

temp = x
x = y
y = temp

print("The Value Of X After Swapping: {}".format(x))
print("The Value Of Y After Swapping: {}".format(y))
