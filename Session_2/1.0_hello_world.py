"""Exercise 1.0: Hello World

WHAT THE PROGRAM MUST DO
    Display a message of your choice, five times, with each line numbered.

ANSWER THESE FIRST, in comments at the top of your file, before any code
    1. What goes in?
    2. What happens to it?
    3. What comes out?
    4. What message did you choose, and why that one?

WHAT THE AI CANNOT KNOW
    The message is yours. Choose something you would actually want a program to say,
    not "Hello, World!". Your comment has to justify it.

CHECK IT YOURSELF
    Count the lines your program produced. Five, not four and not six.
    Then change the number to 3 and run it again. If you had to rewrite more than one
    character, your program is not built the way it should be.

DELIVERABLE
    This file, with your comments and your code.
"""

# 1. In: nothing typed by the user. Two values set in the code:
#    the message to display and how many times to display it.
# 2. Process: a loop repeats the same print, counting from 1 up to the
#    number of repetitions, and puts the counter in front of the message.
# 3. Out: five lines in the terminal, each starting with its number (1 to 5).
# 4. My message, and why: "Hello Skema, I am in Marseille"
#    because it is my first program of the course and it says where I am.


# Your code below
# My variables
message = "Hello Skema, I am in Marseille"
repetitions = 5

for number in range(1, repetitions + 1):
    print(f"{number}. {message}")