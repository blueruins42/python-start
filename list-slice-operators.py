my_list = [1, 2, 4, 4, 1, 4, 2, 6, 2, 9]

new_list = []
for i in range(len(my_list)): # range just extract number not data
    num = my_list[i]
    if num not in new_list:
      new_list.append(num)
for num in my_list:  # it is the elegant way to extract contents in my_list directly
    if num not in new_list:
        new_list.append(num)
      
my_list = new_list[:]
#
print("The list with unique elements only:")
print(my_list)

# in/ not in
my_list = ["a", "b", "c"]
print("A" in my_list)  # False
print("d" not in my_list)  # True

# Review 1
list_1 = ["A", "B", "C"]
list_2 = list_1 # share the memory
list_3 = list_2 # share the memory

del list_1[0] # output ["B", "C"]
del list_2[0] # output [ "C"]

print(list_3) # output [ "C"]

# Review 2
list_1 = ["A", "B", "C"]
list_2 = list_1  # share the memory
list_3 = list_2  # share the memory

del list_1[0] # output ["B", "C"]
del list_2  # list_2 not exists but not affect another two lists

print(list_3) # output ["B", "C"]

# Review 3
list_1 = ["A", "B", "C"]
list_2 = list_1
list_3 = list_2

del list_1[0]
del list_2[:]  # list_2 contents not exist

print(list_3) # output []

# Review 4
list_1 = ["A", "B", "C"]
list_2 = list_1[:]  # list_2 is a new list created to store the content of list_1, not share memory with it
list_3 = list_2[:]  # list_3 is a new list created to store the content of list_2, not share memory with it

del list_1[0] # this step just affect list_1  output [ "B", "C"]
del list_2[0] # this step just affect list_2  output [ "B", "C"]

print(list_3)






