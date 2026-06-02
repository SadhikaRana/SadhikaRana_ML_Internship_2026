# 6.  Swap two number without third variable
a = int(input("Enter first number:"))      # a = 5
b = int(input("Enter second number:"))     # b = 8
a = a + b                                  # a = 13
b = a - b                                  # b = 13 - 8 = 5
a = a - b                                  # a = 13 - 5 = 8
print("After swapping, first number is:", a)
print("After swapping, second number is:", b)
