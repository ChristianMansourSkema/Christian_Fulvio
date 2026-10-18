"""Exercise 3.0: Computing with what the user typed

WHAT THE PROGRAM MUST DO
    Ask for two numbers and display the result of the four operations.

ANSWER THESE FIRST, in comments at the top of your file
    1. What goes in?
    2. What happens to it?
    3. What comes out?
    4. What should your program do when the second number is zero? Decide, write your
       decision down, and only then implement it.

WHAT THE AI CANNOT KNOW
    Your answer to question 4. There are at least three defensible ones: refuse the
    value and ask again, display a message instead of a result, or stop the program.
    Pick one and be able to defend it.

CHECK IT YOURSELF
    Compute 7 divided by 2 in your head. Run your program with 7 and 2. If your program
    shows 3, it is not wrong by accident: find out why, and write the reason in a comment.
    Then run it with 0 as the second number.

DELIVERABLE
    This file, with your comments and your code.
"""

# 1. In: two numbers typed by the user, which arrive as text.
# 2. Process: both are converted to decimal numbers with float(), then
#    added, subtracted, multiplied and divided. Before dividing, the program
#    checks whether the second number is zero.
# 3. Out: four lines, one per operation. For the division, either the result
#    or a message explaining why there is no result.
# 4. What happens when the second number is zero, and why:
#    The program shows a message instead of the division result and still
#    shows the other three. A zero is a valid answer for +, - and *, so
#    stopping would throw away three correct results to avoid one wrong one.
#    Without the check, Python stops everything with ZeroDivisionError.


# Your code below

# input() gives text, float() turns it into a number that can have decimals
first = float(input("First number: "))
second = float(input("Second number: "))

print(f"{first} + {second} = {first + second}")
print(f"{first} - {second} = {first - second}")
print(f"{first} * {second} = {first * second}")

# Dividing by zero has no answer in maths, and makes Python crash.
# Check before dividing, not after
if second == 0:
    print(f"{first} / {second} = impossible, division by zero is not defined")
else:
    print(f"{first} / {second} = {first / second}")
