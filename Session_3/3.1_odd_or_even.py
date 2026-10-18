"""Exercise 3.1: Odd or even (homework)

WHAT THE PROGRAM MUST DO
    Ask the user for a number N, then say for every number from 1 to N whether it is
    odd or even.

ANSWER THESE FIRST, in comments at the top of your file
    1. What goes in?
    2. What happens to it?
    3. What comes out?
    4. What should happen if the user types 0, a negative number, or 5000?
       Decide the three behaviours before writing anything.

WHAT THE AI CANNOT KNOW
    Your three decisions. An assistant asked for "odd or even from 1 to N" will produce
    a program that behaves absurdly on 0 and on -4, and will happily print five thousand
    lines. Those are your calls, not its.

CHECK IT YOURSELF
    Run it with 6. You should see three odd and three even. Count them.
    Then run it with your three edge cases and confirm each does what you decided.

DELIVERABLE
    This file, with your comments and your code.
"""


# 1. In: one whole number N typed by the user.
# 2. Process: N is converted with int(), then checked against my three
#    decisions. If it is between 1 and the limit, a loop goes from 1 to N and
#    looks at the remainder of each number divided by 2: 0 means even,
#    1 means odd.
# 3. Out: one line per number, "1 is odd", "2 is even" ... or a single
#    message explaining why there is no list.
# 4. What happens on 0, on a negative number, on a very large number:
#    - 0: a message, "nothing to check". The range 1 to 0 is empty, and
#      printing nothing at all would look like the program is broken.
#    - negative: a message refusing it and saying what is accepted.
#      "From 1 to -4" has no meaning for this question.
#    - very large (above 100): refused with a message giving the limit.
#      Nobody reads 5000 lines. The limit is in one variable, MAX_N,
#      so it is a one-character change if someone needs more.


# Your code below

# The largest N I accept, kept in one place so it is easy to change
MAX_N = 100

# input() gives text, int() turns it into a whole number
n = int(input("Up to which number? "))

# My three decisions, checked before any loop runs
if n == 0:
    print("0 means there is nothing to check: the range 1 to 0 is empty.")
elif n < 0:
    print(f"{n} is negative. Please give a whole number from 1 to {MAX_N}.")
elif n > MAX_N:
    print(f"{n} is too many lines to read. The limit is {MAX_N}.")
else:
    # range(1, n + 1) goes from 1 to n included
    for number in range(1, n + 1):
        # % gives the remainder: an even number divided by 2 leaves 0
        if number % 2 == 0:
            print(f"{number} is even")
        else:
            print(f"{number} is odd")
