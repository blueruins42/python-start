# python-start

Reframe & Create

## My Python Learning Journey — 2026

As a humanities student, I'm not aiming to become a hardcore programmer. My goal is to build the essential foundational skills needed to navigate the AI era. This repository documents my daily progress in learning Python.

---

## Learning Progress

### Day 1 (2026-02-17)
- Created the `python-start` repository
- Wrote my first Python file using `print()` to output a greeting
- Updated README with initial goals
- **Mood:** Took the first step.
- [Day 1 Code](./day01-say-hello.py)

### Day 2 (2026-02-18)
- Learned variable assignment and f-strings (formatted string literals)
- Understood Python's convention of using double quotes
- [Day 2 Code](./day02-variables.py)

### Day 3 (2026-02-19)
- Learned `input()` for user input and `if / elif / else` for conditional branching
- **Note:** Celebrated my 35th birthday — a small step forward as a gift to myself
- [Day 3 Code](./day03-input-if-else.py)

### Day 4 (2026-02-21)
- Learned lists, `for` loops, and `while` loops for handling multiple data entries
- **Insight:** When multiple concepts combine, it's easy to lose track. Python is a language of structure — only by understanding the structure can you understand the meaning.
- [Day 4 Code](./day04-lists-for-loop.py)

### Day 5 (2026-02-25)
- Successfully pushed code from local VS Code to GitHub — milestone achieved!
- Built a random vocabulary picker using `random.choice()`
- [Day 5 Code](./day05-random-words-player.py)

### PE1- Section 2-2.2 (2026-07-04)
- Restart from Cisco Python Essential 1
- [Python Literals — Strings](./LAB-Python-literals-strings.py): Practice with escape characters, quotes, scientific notation, and boolean comparisons

### PE1- Section 2-2.3 (2026-07-05)
#### What I learned: Python Operators
#### What confused me today
- Why is ** right associative?
- Why does / always return float?
- [Operators - data manipulation tools](./Operators-data-manipulation-tools.py)

### PE1- Section 2-2.4 (2026-07-06)
#### What I learned: Variables — Creating, Naming, and Using
- Learned how to create variables and assign values
- Used `print()` to output variables, including combining multiple variables with commas
- Combined text and variables using the `+` operator (string concatenation)
- **Insight:** The textbook says you can use `print()` with `+` to combine text and variables — and it works perfectly when both sides are strings. But the moment you try to combine a number with a string (e.g., `print("Score: " + 95)`), Python throws a `TypeError`. This is because the `+` operator in Python is type-sensitive: it performs arithmetic on numbers (int/float) and concatenation on strings (str), but it cannot implicitly convert between the two. You must explicitly convert numbers to strings using `str()` first, e.g., `print("Score: " + str(95))`. This is a fundamental difference from languages like JavaScript, where `+` auto-coerces types.
- [Variables - create, use, name](./variables-create-use-name.py)

### PE1- Section 2-2.48 (2026-07-07)
#### Mistakes I Made
- Misunderstood the evaluation order of `/=`.
#### What I Learned
- Compound assignment is just shorthand for a normal assignment.
- Always expand `+=`, `-=`, `*=`, `/=` mentally before evaluating an expression.
- [variables-Operators-expressions](./variables-Operators-expressions.py)

### PE1- Section 2-2.6 (2026-07-08)
#### What I Learned
- input() function
#### Key takeaways:
- input() always pauses execution until the user presses Enter.
- The prompt argument is only a message for the user, not the input value itself.
- input() always returns a string, so numeric calculations require type conversion (e.g., int() or float()).
- [interact-with-user](./interact-with-user.py)

### PE1- Section 3-3.17 (2026-07-09)
#### What I Learned
- Questions and Answers: True/False
- Comparison:equality operator
- Conditional Exection:if/else statements
#### Note:
- if there is more than one instruction in the indented part, the indentation should be the same in all lines;
- even though it may look the same if you use tabs mixed with spaces, it's important to make all indentations exactly the same – Python 3 does not allow the mixing of spaces and tabs for indentation.
- [if-else-statement](./if-else-statement.py)

### PE1- Section 3-3.19 (2026-07-10)
#### What confused me today
- how pseudocode is presented to help form a basic, initial computing mindset.
#### What I Learned
- Conditional Exection:elif statement
- [Pseudocode](./Pseudocode.py)
---

## Goals

| Timeframe | Goal |
|-----------|------|
| **Short-term** | Learn basic web scraping to collect information sources |
| **Mid-term** | Build a web-based chatbot with interactive capabilities |
| **Long-term** | Deploy an open-source LLM locally (e.g., GLM-5) and fine-tune a personal chatbot |

---

## Tech Stack

- **Language:** Python 3
- **Editor:** VS Code (local push to GitHub)
- **Platform:** GitHub

---

*This repository is a living document. Updated as I learn.*
