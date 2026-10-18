"""Exercise 8.0: Operators (bonus, not graded)

WHAT THE PROGRAM MUST DO
    Take two values of your choice and display, as a readable table, the result of every
    comparison between them and of the logical combinations of those results.

ANSWER THESE FIRST, in comments
    1. What goes in?
    2. What happens to it?
    3. What comes out?
    4. Which two values did you pick, and which comparison result surprised you?

WHAT THE AI CANNOT KNOW
    Your two values. Pick a pair where the answer is not obvious: two strings with
    different capitalisation, a number and the same number written as text, or zero and
    an empty string.

CHECK IT YOURSELF
    Predict each result before running. Count how many you got right.

DELIVERABLE
    This file, with your comments and your code.
"""



# 1. In: two values set in the code: "Paris" and "paris".
# 2. Process: Python compares them with the six comparison operators
#    (== != < > <= >=), then combines two of those results with and, or, not.
# 3. Out: a two-column table, each expression and its result (True or False).
# 4. My two values, and the result that surprised me:
#    "Paris" and "paris", the same city typed two ways, as in a messy
#    customer file. Surprise: "Paris" < "paris" is True. Strings are compared
#    by character code, and every capital comes before every lowercase letter
#    (P = 80, p = 112).


# Your code below

# The two values 
a = "Paris"
b = "paris"

# Two results kept in variables, to combine them with and / or / not below
equal = a == b
less = a < b

print(f"Comparing a = {a!r} and b = {b!r}")
print()

# :<28 pads the text to 28 characters, so the results line up in a  column
print(f"{'Expression':<28}Result")
print("-" * 36)

# The six comparisons
print(f"{'a == b':<28}{a == b}")
print(f"{'a != b':<28}{a != b}")
print(f"{'a < b':<28}{a < b}")
print(f"{'a > b':<28}{a > b}")
print(f"{'a <= b':<28}{a <= b}")
print(f"{'a >= b':<28}{a >= b}")
print("-" * 36)

# The logical combinations
print(f"{'(a == b) and (a < b)':<28}{equal and less}")
print(f"{'(a == b) or (a < b)':<28}{equal or less}")
print(f"{'not (a == b)':<28}{not equal}")

# The fix for real data
print(f"{'a.lower() == b.lower()':<28}{a.lower() == b.lower()}")
