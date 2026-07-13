# design a vowel eater!
# for-if-continue
user_word = input("enter a word: ")
user_word = user_word.upper()

for letter in user_word:
    if letter in "AEIOU":
          continue
    print(letter)

# break
while True:
  word = input("Enter a word:")
  if word == "chupacabra"
  print("You've successfully left the loop.")
        break
# pyramid
blocks = int(input("Enter the number of blocks: "))

height = 0
current_layer = 1

while blocks >= current_layer:
    blocks = blocks - current_layer
    height += 1
    current_layer += 1
    	
print("The height of the pyramid:", height)
