# Operators and expressions
x = 0
x = float(x)
y = 3 * x**3 - 2 * x**2 + 3 * x - 1
print("y =", y)

x = 1
x = float(x)
y = 3 * x**3 - 2 * x**2 + 3 * x - 1
print("y =", y)

x = -1
x = float(x)
y = 3 * x**3 - 2 * x**2 + 3 * x - 1
print("y =", y)

# Shortcut operators
i = i + 2 * j
i += 2 * j
var = var / 2
var /= 2
rem = rem % 10
rem %= 10
j = j - (i+ var + rem)
j -= (i + var + rem)
x = x ** 2
x **= 2

# operate order
a = 6
b = 3
a /= 2 * b
print(a)
a = a / (2 * b)
