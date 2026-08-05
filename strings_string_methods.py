# Python's strings are immutable. don't allow you to use the del instruction to remove anything from a string.
alphabet = "abcdefghijklmnopqrstuvwxyz"
del alphabet[0]   # error
del alphabet   # correct
# don't have the append() method – you cannot expand them in any way.
alphabet.append("A") # error 
# the insert() method is illegal
alphabet.insert(0, "A")

alphabet = "bcdefghijklmnopqrstuvwxy"

# allowed to do
alphabet = "a" + alphabet
alphabet = alphabet + "z"

print(alphabet)   #  abcdefghijklmnopqrstuvwxyz

# index() method returns the index of the first occurrence of the argument
print("aAbByYzZaA".index("b"))  # 2
print("aAbByYzZaA".index("Z"))   # 7
print("aAbByYzZaA".index("A"))   # 1

# list() function takes its argument (a string) and creates a new list containing all the string's characters, one per list element.
print(list("abcabc"))   # ['a', 'b', 'c', 'a', 'b', 'c']

# count() method counts all occurrences of the element inside the sequence.
print("abcabc".count("b"))  # 2
print('abcabc'.count("d"))   # 0

# capitalize() method
print('aBcD'.capitalize())  # Abcd
print("Alpha".capitalize())  # Alpha
print('ALPHA'.capitalize()) # Alpha
print(' Alpha'.capitalize())  # space alpha
print('123'.capitalize())    # 123
print("αβγδ".capitalize())   # Αβγδ

# center() method
print('[' + 'alpha'.center(10) + ']')   # one-parameter variant :  [  alpha   ]
print('[' + 'Beta'.center(2) + ']')   # [Beta]
print('[' + 'Beta'.center(4) + ']')   # [Beta]
print('[' + 'Beta'.center(6) + ']')   # [ Beta ]
print('[' + 'gamma'.center(20, '*') + ']')   # two-parameter variant : [*******gamma********]

# endswith() method
t = "zeta"
print(t.endswith("a"))   # True
print(t.endswith("A"))  # False
print(t.endswith("et"))  # False
print(t.endswith("eta"))   # True

# find() method: similar to index() method, but returns 1 or -1
print("aEta".find("ta"))   # 2
print("Eta".find("mma"))   # -1 : don't generate error when containing a non-existence substring

print('kappa'.find('a', 2))  # 4  start will string[2]

the_text = """A variation of the ordinary lorem ipsum
text has been used in typesetting since the 1960s 
or earlier, when it was popularized by advertisements 
for Letraset transfer sheets. It was introduced to 
the Information Age in the mid-1980s by the Aldus Corporation, 
which employed it in graphics and word-processing templates
for its desktop publishing program PageMaker (from Wikipedia)"""

fnd = the_text.find('the')
while fnd != -1:
    print(fnd)
    fnd = the_text.find('the', fnd + 1)
# 15
# 80
# 198
# 221
# 238

print('kappa'.find('a', 1, 4))    # 1 'app' find a between [start, end], not involve end
print('kappa'.find('a', 2, 4))    # -1 'pp'
