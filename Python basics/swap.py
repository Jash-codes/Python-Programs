#  getting input from user

a = int(input("enter the first number(a) : "))

b = int(input("enter the second number(b): "))

print(f"before swapping: a={a},b={b}")

temp = a
a = b
b = temp

print(f"after swapping : a={a},b={b}")