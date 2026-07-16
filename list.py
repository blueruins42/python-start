# step 1
beatles = [] # create an empty list named beatles;

print("Step 1:", beatles)

# step 2 
beatles.append("John Lennon")
beatles.append("Paul McCartney")
beatles.append("George Harrison")

print("Step 2:", beatles)

# step 3
for i in range(2): # use the for loop and the append() method 
    name = input("Enter a new name:")
    beatles.append(name)
    
print("Step 3:", beatles)

# step 4 use the del instruction
del beatles[4]
del beatles[3]

print("Step 4:", beatles)

# step 5 use the insert() method 
beatles.insert(0, "Ringo Starr")
print("Step 5:", beatles)


# testing list legth
print("The Fab", len(beatles))

