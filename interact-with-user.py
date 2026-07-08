# input() function, the input is always a string. If you want to use it as a number, you need to convert it to an integer or float.
anything = input("Enter a number: ")
something = int(anything) ** 2.0
print(anything, "to the power of 2 is", something)

fnam = input("May I have your first name, please? ")
lnam = input("May I have your last name, please? ")
print("Thank you.")
# need to generate new strings
print("\nYour name is " + fnam + " " + lnam + ".")
# only print all arguments
print("\nYour name is", fnam, lnam, sep=" ", end=".")

print("+" + 10 * "-" + "+")
# string appended after the last value, default a newline.
print(("|" + " " * 10 + "|\n") * 5, end="")
print("+" + 10 * "-" + "+")

# We can pass the whole result to the print() function as one string, forgetting about the commas.
leg_a = float(input("Input first leg length: "))
leg_b = float(input("Input second leg length: "))
print("Hypotenuse length is " + str((leg_a**2 + leg_b**2) ** .5))

leg_a = float(input("Input first leg length: "))
leg_b = float(input("Input second leg length: "))
print("Hypotenuse length is", (leg_a**2 + leg_b**2) ** .5)

# input a float value for variable a here
a = float(input("set a number here..."))
# input a float value for variable b here
b = float(input("add another number here..."))
# output the result of addition here
print(a + b)
# output the result of subtraction here
print(a - b)
# output the result of multiplication here
print(a * b)
# output the result of division here
print(a / b)
print("\nThat's all, folks!")

print(type(1))
print(type(1.))

print(1 / 2)
print(1. / 2)

print(1 / 2.)
print(1. / 2.))

hours = int(input("Starting time (hours): "))
minutes = int(input("Starting time (minutes): "))
duration = int(input("Duration (minutes): "))
total_minutes = hours * 60 + minutes + duration
new_hours = (total_minutes // 60) % 24
new_minutes = total_minutes % 60
print("New time is %02d:%02d" % (new_hours, new_minutes))
