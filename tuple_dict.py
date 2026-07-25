# dict exercise
dictionary = {"cat": "chat", "dog": "chien", "horse": "cheval"}

for key in dictionary.keys():
    print(key, "->", dictionary[key])

for french in dictionary.values():
    print(french)

for english, french in dictionary.items():
    print(english,french)

dictionary['cat'] = 'mioun'
print(dictionary)
for key in sorted(dictionary.keys()):
    print(dictionary)
dictionary.update({'apple':1})
dictionary['banana'] = '01'

dictionary.popitem()
dictionary_copy = dictionary.copy()
print(dictionary_copy)
dictionary.clear()
print(dictionary)
del dictionary

# tuple
# Example 1
tuple_1 = (1, 2, 3)
for elem in tuple_1:
    print(elem)

# Example 2
tuple_2 = (1, 2, 2,3, 2,4)
number = tuple_2.count(2)
print("number:",number)
print(5 in tuple_2)
print(5 not in tuple_2)

# Example 3
tuple_3 = (1, 2, 3, 4)
print(len(tuple_3))
print(5 not in tuple_3)
# Example 4
tuple_4 = tuple_1 + tuple_2   # glue two tuple
tuple_5 = tuple_3 * 2 # duplicate tuple

print(tuple_4)
print(tuple_5)


