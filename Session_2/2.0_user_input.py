"""Exercise 2.0: Asking the user

WHAT THE PROGRAM MUST DO
    Ask the user for two pieces of information, then display a sentence that uses both.

ANSWER THESE FIRST, in comments at the top of your file
    1. What goes in?
    2. What happens to it?
    3. What comes out?
    4. Which two pieces of information did you choose, and for what purpose?
       Imagine a real form in your future job. Not "name and age" unless you can
       say what you would do with them.

WHAT THE AI CANNOT KNOW
    Your two fields, and the sentence you want at the end. Decide both before you ask.

    One of your two values will almost certainly need to be a number. Find out what
    happens when you try to add 1 to something the user typed, and deal with it.

CHECK IT YOURSELF
    Run your program and answer with an empty line. Then with a space. Then with text
    where you expected a number. Write in a comment what happened each time.
    You are not asked to fix it yet, only to see it.

DELIVERABLE
    This file, with your comments and your code.
"""


# 1. In: two answers typed by the user: their weight in kilograms and
#    their height in centimetres.
# 2. Process: both answers arrive as text, so they are converted to
#    decimal numbers with float(). The height is turned into metres
#    (divided by 100), then BMI = weight / (height in metres squared).
# 3. Out: one sentence with both values and the BMI rounded to one decimal, e.g.
#    "For 70.0 kg and 175.0 cm, your BMI is 22.9."
# 4. My two fields, and what I would do with them:
#    The first screen of a sports or health app. Weight and height give the BMI,
#    a quick first indicator used to adapt the advice or the program offered.


# Your code below

# Ask the two questions
weight_text = input("Your weight in kg: ")
height_text = input("Your height in cm: ")


# float, not int, because a weight like 70.5 has decimals
weight = float(weight_text)
height_cm = float(height_text)

# The BMI formula uses metres, so we do the conversion from cm to m
height_m = height_cm / 100
bmi = weight / height_m ** 2

# One sentence that uses both values, BMI rounded to one decimal
print(f"For {weight} kg and {height_cm} cm, your BMI is {round(bmi, 1)}.")
