# Day 5 (2026-02-25): Local push test successful! Back on track.

import random

# Your vocabulary bank (add more anytime)
words = [
    ("synthetic", "artificial, man-made"),
    ("perennial", "long-lasting, enduring"),
    ("artificial", "man-made, not natural"),
    ("cognition", "the process of knowing, perception"),
    ("evolution", "gradual development, progression"),
    ("wakeup", "to awaken, to become aware"),
]

# Pick a random word
word, meaning = random.choice(words)

print("Today's word:")
print(f"  {word}")
print(f"  Meaning: {meaning}")

input("\nPress Enter to end today's 'learning ritual' ~")
print("Done! See you tomorrow ~")
