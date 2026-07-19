def subtra(a, b):
    print(a - b)

subtra(5, b=2)    # outputs: 3
subtra(a=5, 2)    # Syntax Error

# it is allowed to use the keyword argument-passing technique to pre-define a value for a given argument:
def name(first_name, last_name="Smith"):
    print(first_name, last_name)

name("Andy")    # outputs: Andy Smith
name("Betty", "Johnson")    # outputs: Betty Johnson (the keyword argument replaced by "Johnson")

# The mistake I made
def number():
    print("Enter a value:")

number()
a = 4
number()
b = 7
number()
c = 9

def method():
    a += b    # UnboundLocalError: cannot access local variable 'a' where it is not associated with a value

method()
print(a)

# Correction
def number():
    print("Enter a value:")

number()
a = 4
number()
b = 7
number()
c = 9

# a,b used as arguments passing into function and give values to parameters
def method(x, y):
    return x + y # tell function to do addition operator and reture the result

a = method(a, b) # pass the value calculated from method (x,y) to variable a

print(a)  # 输出 11
