# Sample code
def is_a_triangle(a, b, c):
    return a + b > c and b + c > a and c + a > b
 
 
def heron(a, b, c):
    p = (a + b + c) / 2
    return (p * (p - a) * (p - b) * (p - c)) ** 0.5
 
 
def area_of_triangle(a, b, c):
    if not is_a_triangle(a, b, c):
        return None
    return heron(a, b, c)
 
 
print(area_of_triangle(1., 1., 2. ** .5))

# why not combine def heron() and def area_of_triangle?
def heron(a, b, c):
    if not is_a_triangle(a, b, c):
        return None
    p = (a + b + c) / 2
    return (p * (p - a) * (p - b) * (p - c)) ** 0.5
def is_a_triangle(a, b, c):
    return a + b > c and b + c > a and c + a > b

print(heron(1., 1., 2. ** .5))

# the disorder mistake
# Name_error: is_a_triangle is not defined. Why?
def heron(a, b, c):
    if not is_a_triangle(a, b, c):
        return None
    p = (a + b + c) / 2
    return (p * (p - a) * (p - b) * (p - c)) ** 0.5

print(heron(1., 1., 2. ** .5)) # this step cannot be surpassed by def is_a_triangle()
# Python doesn't have already read this funciton in its memory though it won't be executed until invoke
def is_a_triangle(a, b, c):
    return a + b > c and b + c > a and c + a > b

