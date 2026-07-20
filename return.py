def boring_function(a):
    print ("the result is", a) # output the value (90)from invocation of funciton
    return 123

print("This lesson is interesting!")

print(boring_function(90))  # output the value (123) from return
print("This lesson is boring...")


def strange_function(n):
    if n % 2 == 0:
       return True 
print(strange_function(2))  # True
print(strange_function(1))  # None

def strange_function(n):
    if n % 2 == 0:
       return True 
    else:
       return False
print(strange_function(2))  # True
print(strange_function(1))  # False 

# Three Comparison Exercise
# the optimal 
def strange_list_fun(n):
    strange_list = []
    
    for i in range(0, n):
        strange_list.insert(0, i)

    return strange_list  # output the list and print outside the loop

print(strange_list_fun(5))

# the basic
def strange_list_fun(n):
    strange_list = []
    
    for i in range(0, n):
        strange_list.insert(0, i)
    
    print("return", strange_list)  # also output result of [4,3,2,1,0] However it is weaker for latter optimization
strange_list_fun(5)

# the wrong pattern
def strange_list_fun(n):
    strange_list = []
    print("return", strange_list)  # it returns [], because the time spot here is nothing
    for i in range(0, n):          # actually for loop is running
        strange_list.insert(0, i)
                                  # the time spot here is none, no print result
strange_list_fun(5)
