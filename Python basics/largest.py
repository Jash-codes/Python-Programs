a = float(input("Enter the first number : "))   # Taking input from user
b = float(input("Enter the second number : "))
c = float(input("Enter the third number : "))

if a>=b and a>=c:  ## condition to find largest
    largest = a
elif b>=a and b>=c:
    largest  = b
else:
    largest = c

print(f"The largest among {a}, {b}, {c} is {largest}")

