# list reass
def my_function(my_list_1):
    print("Print #1:", my_list_1)  # output [2.3]  outside list
    print("Print #2:", my_list_2)  # output [2.3]  outside list
    my_list_1 = [0, 1]   # rebuild a box to store a new value
    print("Print #3:", my_list_1)  # output [0,1]  use the new box value
    print("Print #4:", my_list_2)  # output [2.3]  outside list

my_list_2 = [2, 3]
my_function(my_list_2)
print("Print #5:", my_list_2)   # output [2.3]

# modify the list identified by it
def my_function(my_list_1):
    print("Print #1:", my_list_1)  # output [2.3]
    print("Print #2:", my_list_2)  # output [2.3]
    del my_list_1[0]  # del keyword modify the list itself and it reflects the following output
    print("Print #3:", my_list_1)  # output [3]  list doesn't duplicate the list value, recap the slice and list
    print("Print #4:", my_list_2)  # output [3]

my_list_2 = [2, 3]
my_function(my_list_2)
print("Print #5:", my_list_2)  # output [3]

# Name error scope
def message():
    alt = 1
    print("Hello, World!")

print(alt) # cannot use the variable inside the function body

# inside or outside the function both defined situation
a = 1

def fun():
    a = 2
    print(a)

fun()   # use the inside function variable  a = 2
print(a)  # use the outside variable a = 1

# keyword global
a = 1

def fun():
    global a   # when invoke the function once it excutes replacing 1 with 2 outside 
    a = 2
    print(a)  # output 2

fun()  # until this step, a = 2
a = 3  # a soon is assigned to 3 again
print(a)  # output 2

a = 1

def fun():
    global a
    a = 2
    print(a)  # output 2

a = 3   # until this step, a = 3
fun()   # when invoke the function once it excutes replacing 3 with 2 outside 
print(a) # output 2 notice: it changes the outside variable directly



